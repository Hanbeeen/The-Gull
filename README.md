# 🛠️ THE-GULL: Slack Bot for Analyzing Participation and Contribution in Team Projects using NLP

> **Team MATE**  
> **Project Duration**: Sep 2024 – Dec 2024  
> **Mentor Organization**: IBM  
> **Supervisor**: Prof. Manjae Kim (Dept. of AI, Chonnam National University)  
> **Team Members**: Hanbin Im (Team Leader), Jaeoh Seo  

---

## 📌 Overview

**THE-GULL** is a Slack Bot that uses natural language processing (NLP) to analyze participation and contribution in team projects.  
It aims to promote fair collaboration by visualizing each member’s level of engagement and providing transparent, data-driven feedback on performance.
https://youtu.be/9yCiiAUoqdg

### 🔍 Motivation

Team projects, especially in academic settings, often suffer from uneven participation, leading to dissatisfaction and conflict.  
Inspired by the **Ringelmann Effect**, this project addresses the issue by objectively analyzing member contributions, thereby encouraging balanced participation and enhancing teamwork.

---

## 🎯 Key Features

### 1. Participation Analysis
- **Metrics**: Number of messages, total speech volume, emoji reactions.
- **Command Examples**: `/message_count`, `/reaction_count`, `/speech_volume`
- Visualized dashboards display each member's activity.
- ![image](https://github.com/user-attachments/assets/67ebcbd5-8ca0-4b88-a114-3e39d9bb2696)

### 2. Contribution Analysis
- **Metrics**: Topic relevance (semantic similarity), meeting facilitation score.
- **Command Examples**: `/topic_similarity`, `/meeting_contribution`
- Uses transformer-based models (LLaMA 3, mBERT) served via IBM Watsonx.ai.
- ![image](https://github.com/user-attachments/assets/c8123478-f280-4932-afee-d1a3bb95ef12)

### 3. Team Leader Recommendation
- Scores members based on their facilitation role in meetings.
- Recommends the most active and leading member as a suitable team leader.
- ![image](https://github.com/user-attachments/assets/d1c72181-5f51-401e-ad80-7159272f450b)

### 4. GUI-Based Environment Setup
- Electron + Docker-based GUI automates:
  - Local server setup
  - Slack Bot installation
  - API tunneling
- Accessible even to non-technical users.
- ![image](https://github.com/user-attachments/assets/5c0e84c8-9d16-4e23-a97f-c2f6fdd7ad7b)

---

## 🧪 System Architecture

![image](https://github.com/user-attachments/assets/12e7e49e-05db-47cc-8089-33461c417f01)

- Slack → Log Scraping → NLP Engine (Watsonx.ai) → Contribution Analysis
- Electron GUI → Server Control Panel → Docker + API tunneling

---

## 📊 Visual Feedback Samples

### PC Interface  
![image](https://github.com/user-attachments/assets/71364187-dac0-4d9f-9fae-8cee2a206daf)

### Mobile Interface  
![image](https://github.com/user-attachments/assets/f5c2e0c2-e468-4de4-8230-3ceff8f7eaf1)


---

## 🧠 Technologies Used

- **Slack API** – Message log collection  
- **Watsonx.ai** – LLM inference (LLaMA3, mBERT)  
- **Electron** – GUI interface for bot control  
- **Docker** – Environment containerization  
- **Python** – Backend implementation  
- **KMeans**, **Sentence Embedding**, **Sentiment Analysis** (future expansion)

---

## 💡 Expected Impact

- **Promotes Data-Driven Teamwork**: Objective performance evaluation using NLP  
- **Reduces Group Work Anxiety**: Transparent analysis mitigates unfair workload  
- **Scalable Use Cases**:  
  - Plug-in for other collaboration tools  
  - Integration with HR tools  
  - Educational platforms for project assessment  
- **Future Development Plans**:
  - Real-time scheduling recommendations  
  - Contribution dashboard  
  - Emotion-aware contribution scoring  
  - Beta release and open-source distribution

---

## 🔄 How to Run

> ⚙️ A GUI-based `.exe` file is provided for local server setup.

1. Run Electron GUI  
2. Slack token + workspace input  
3. Automatically sets up server, tunneling, and bot launch

---

## 🔗 References

- [Slack API Docs](https://api.slack.com/docs)  
- [Intro to NLP with Deep Learning (WikiDocs)](https://wikidocs.net/book/2155)  
- [Docker Documentation](https://docs.docker.com/)  
- Related Startup: [Agigorae – SaaS for Organizational Culture](https://magazine.hankyung.com/job-joy/article/202312213771d)

---

## 🧑‍💻 Contributors

| Name | Role | GitHub |  
|------|------|--------|  
| **Hanbin Im** | Project Lead, NLP & Slack Bot Development | [@Hanbeeen](https://github.com/Hanbeeen) |  
| **Jaeoh Seo** | Backend, Electron GUI, Infrastructure Setup | [@seojaeohcode](https://github.com/seojaeohcode) |  

---

## 📌 License

MIT License – Open-source version to be released after beta testing.
