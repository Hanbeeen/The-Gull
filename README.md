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

### 🔍 Motivation

Team projects, especially in academic settings, often suffer from uneven participation, leading to dissatisfaction and conflict.  
Inspired by the **Ringelmann Effect**, this project addresses the issue by objectively analyzing member contributions, thereby encouraging balanced participation and enhancing teamwork.

---

## 🎯 Key Features

### 1. Participation Analysis
- **Metrics**: Number of messages, total speech volume, emoji reactions.
- **Command Examples**: `/message_count`, `/reaction_count`, `/speech_volume`
- Visualized dashboards display each member's activity.

### 2. Contribution Analysis
- **Metrics**: Topic relevance (semantic similarity), meeting facilitation score.
- **Command Examples**: `/topic_similarity`, `/meeting_contribution`
- Uses transformer-based models (LLaMA 3, mBERT) served via IBM Watsonx.ai.

### 3. Team Leader Recommendation
- Scores members based on their facilitation role in meetings.
- Recommends the most active and leading member as a suitable team leader.

### 4. GUI-Based Environment Setup
- Electron + Docker-based GUI automates:
  - Local server setup
  - Slack Bot installation
  - API tunneling
- Accessible even to non-technical users.

---

## 🧪 System Architecture

![System Overview](https://github.com/user-attachments/assets/d7477ff5-233d-465a-b06e-1e5ceb5489fb)

- Slack → Log Scraping → NLP Engine (Watsonx.ai) → Contribution Analysis
- Electron GUI → Server Control Panel → Docker + API tunneling

---

## 📊 Visual Feedback Samples

### PC Interface  
![PC Screenshot](https://github.com/user-attachments/assets/8dc7e680-c262-42ea-b47e-49e3c9cd4fc4)

### Mobile Interface  
![Mobile Screenshot](https://github.com/user-attachments/assets/93bcd807-54bd-4c46-a4a6-f574601f8ace)

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
