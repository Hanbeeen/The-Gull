import threading
import json
import os
from flask import Flask, request, make_response
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from datetime import datetime
from dotenv import load_dotenv

# .env 파일에서 환경 변수 로드
load_dotenv()

app = Flask(__name__)

# .env 파일에서 SLACK_BOT_TOKEN을 불러옴
token = os.getenv("SLACK_BOT_TOKEN")
print(f"SLACK_BOT_TOKEN: {token}")  # 확인용 출력

# Slack WebClient 설정
if token:
    client = WebClient(token)
    print("Slack client initialized")
else:
    print("SLACK_BOT_TOKEN is not set!")

@app.route('/', methods=['POST'])
def hello_there():
    slack_event = json.loads(request.data)
    
    # Slack에서 온 'challenge' 요청을 처리하고 응답
    if "challenge" in slack_event:
        return make_response(slack_event["challenge"], 200, {"Content-Type": "application/json"})
    
    return make_response("There are no slack request events", 404, {"X-Slack-No-Retry": 1})

# '/hello' Slash Command 처리 라우트
@app.route('/hello', methods=['POST'])
def slash_hello():
    slack_event = request.form  # Slash command는 form data로 전달됨
    print(f"Received event: {slack_event}")  # 이벤트 데이터를 출력하여 확인
    
    channel_id = slack_event.get('channel_id')  # 명령어가 발생한 채널 ID
    print(f"Channel ID: {channel_id}")  # 채널 ID 출력

    # Slash Command '/hello' 처리
    if slack_event.get('command') == '/인사':  # 명령어가 '/hello'일 때
        try:
            # chat.postMessage API를 통해 채널에 메시지 보내기 (봇이 보냄)
            response = client.chat_postMessage(
                channel=channel_id,  # 메시지를 보낼 채널 ID
                text="Hello, everyone!",  # 메시지 내용
                username="데굴이",  # 봇의 사용자명을 "데굴이"로 변경
                icon_emoji=":bird:"  # 봇의 아이콘 설정 (이모지)
            )
            return make_response("Message sent to the channel", 200)
        
        except SlackApiError as e:
            print(f"Slack API error: {e.response['error']}")  # 에러 메시지 출력
            error_message = f"Error sending message: {e.response['error']}"
            return make_response(error_message, 500)
    
    return make_response("Command not recognized", 404)


# 타임스탬프를 사람이 읽을 수 있는 형식으로 변환하는 함수
def convert_timestamp_to_readable(ts):
    return datetime.utcfromtimestamp(float(ts)).strftime('%Y-%m-%d %H:%M:%S')

# 채널 채팅 로그를 가져오는 통합 함수 (전체, 사용자, 봇 메시지 필터링) 
# target을 user나 bot으로 지정하면 해당 타겟에 맞는 내역만 가져옴.(EX:user = user채팅내역만 가져옴.)
# 인수를 넣지 않으면 모든 채팅내역을 가져옴.
def get_chatlog(channel_id, target='all'):
    try:
        chat_logs = []
        has_more = True
        next_cursor = None
        
        # 현재 봇의 user_id를 가져옴
        auth_response = client.auth_test()
        bot_user_id = auth_response['user_id']
        
        while has_more:
            # conversations.history API를 통해 채널 메시지 기록 가져오기
            result = client.conversations_history(
                channel=channel_id,
                cursor=next_cursor  # 페이지네이션을 위한 cursor
            )
            
            # 메시지 리스트를 가져옴
            messages = result["messages"]
            
            # 각 메시지 필터링
            for message in messages:
                user_id = message.get('user')
                
                # 사용자 정보를 가져옴
                user_info = client.users_info(user=user_id)
                username = user_info['user']['name']
                
                # target에 따라 필터링
                if target == 'user':
                    # 봇 메시지는 제외
                    if user_id == bot_user_id:
                        continue
                elif target == 'bot':
                    # 봇 메시지만 포함
                    if user_id != bot_user_id:
                        continue
                
                # 메시지를 chat_logs에 추가 (username 포함)
                chat_logs.append({
                    "user_id": user_id,
                    "username": username,
                    "text": message.get('text'),
                    "timestamp": message.get('ts')
                })
            
            # 페이지네이션 정보 업데이트
            has_more = result.get('has_more', False)
            next_cursor = result.get('response_metadata', {}).get('next_cursor')
        
        return chat_logs  # 필터링된 메시지 로그 리턴
    
    except SlackApiError as e:
        print(f"Slack API error: {e.response['error']}")
        return None
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        return None


# 채팅 로그 가져오기 및 메시지 전송 작업 (비동기 실행)
def send_chat_log_to_slack(channel_id, target):
    # bot의 메시지 내역만 가져오기
    chat_logs = get_chatlog(channel_id, target)

    print(chat_logs)

    if chat_logs is None:
        client.chat_postMessage(
            channel=channel_id,
            text="Error fetching chat log"
        )
        return

    # chat_log의 각 항목에서 ID, text, timestamp, username을 포함하여 메시지를 포맷
    formatted_chat_log = "\n".join([f"ID: {log['user_id']}, Username: {log['username']}, Time: {convert_timestamp_to_readable(log['timestamp'])}, Message: {log['text']}" for log in chat_logs])

    # 메시지가 너무 길 경우 4000자 단위로 나눠서 보냄
    for i in range(0, len(formatted_chat_log), 4000):
        client.chat_postMessage(
            channel=channel_id,  # 메시지를 보낼 채널 ID
            text=f"Here is the bot chat history:\n{formatted_chat_log[i:i+4000]}"  # 채팅 기록
        )

# botchatlog 라우트 처리
@app.route('/botchatlog', methods=['POST'])
def bot_chatlog():
    slack_event = request.form  # Slash command는 form data로 전달됨
    channel_id = slack_event.get('channel_id')  # 명령어가 발생한 채널 ID 가져오기

    # 먼저 200 응답을 반환하여 타임아웃을 방지
    response = make_response("Processing chat log...", 200)
    
    # 비동기 작업으로 채팅 로그 가져오기 및 메시지 전송 실행
    threading.Thread(target=send_chat_log_to_slack, args=(channel_id, 'bot')).start()

    return response

# 발화량 분석 및 메시지 전송 작업 (비동기 실행)
def send_speech_analysis_to_slack(channel_id):
    chat_logs = get_chatlog(channel_id, target='user')

    if chat_logs is None:
        client.chat_postMessage(
            channel=channel_id,
            text="Error fetching chat log"
        )
        return
    
    print(chat_logs)

    # 발화량 분석: 사용자별 메시지 수를 계산
    user_message_count = {}
    
    for log in chat_logs:
        user_id = log['user_id']
        user_message_count[user_id] = user_message_count.get(user_id, 0) + 1

    # 가장 많이 발화한 사용자 찾기
    most_active_user = max(user_message_count, key=user_message_count.get)
    most_active_count = user_message_count[most_active_user]

    # 결과 메시지를 Slack 채널에 보내기
    client.chat_postMessage(
        channel=channel_id,
        text=f"User <@{most_active_user}> has spoken the most with {most_active_count} messages."
    )

# speechquantity 라우트 처리
@app.route('/speechquantity', methods=['POST'])
def speechquantity():
    slack_event = request.form  # Slash command는 form data로 전달됨
    channel_id = slack_event.get('channel_id')  # 명령어가 발생한 채널 ID 가져오기

    # 먼저 200 응답을 반환하여 타임아웃을 방지
    response = make_response("Processing speech analysis...", 200)
    
    # 비동기 작업으로 발화량 분석 실행
    threading.Thread(target=send_speech_analysis_to_slack, args=(channel_id,)).start()

    return response

# 테스트용 라우트 추가
@app.route('/network', methods=['GET'])
def test():
    return "Hello, World!", 200

if __name__ == '__main__':
        # 환경 변수를 사용하여 호스트와 포트를 설정 (기본값은 0.0.0.0과 5000)
    host = os.getenv('FLASK_RUN_HOST', '0.0.0.0')
    port = int(os.getenv('FLASK_RUN_PORT', 5000))
    app.run(host=host, port=port)