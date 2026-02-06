# LangGraph Multi-Agent Knowledge Bot

## 📌 Project Overview

This project is a **LangGraph-based Multi-Agent Knowledge Bot** built using **Python** and **FastAPI**.  
It demonstrates how multiple AI agents collaborate to process user queries using a graph-based workflow and generate intelligent responses.

The application exposes a REST API that allows users to submit questions and receive AI-generated answers.

---

## 📁 Project Structure

langgraph-multi-agent-knowledge-bot/
├── api/
│ ├── main.py # FastAPI application entry point
│ ├── graph/
│ │ └── agent_graph.py # LangGraph workflow definition
│ └── agents/
│ └── init.py # Agent logic (extendable)
├── requirements.txt # Project dependencies
├── README.md # Project documentation
└── .gitignore

---

## ⚙️ Setup Instructions

### 1️⃣ Prerequisites

Make sure you have the following installed:

- Python 3.10 or 3.11  
- Git  
- Internet connection  

---

### 2️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/langgraph-multi-agent-knowledge-bot.git
cd langgraph-multi-agent-knowledge-bot

3️⃣ Create Virtual Environment
Activate the environment:

Windows

venv\Scripts\activate


Linux / macOS

source venv/bin/activate

4️⃣ Install Dependencies
pip install -r requirements.txt

▶️ How to Run the Project

From the project root directory, run:

uvicorn api.main:app --reload


Server will start at:

http://127.0.0.1:8000

🌐 API Usage
Swagger UI

Open your browser and go to:

http://127.0.0.1:8000/docs


You can:

View available APIs

Test requests interactively

See request & response formats

Sample API Endpoint

POST /query

Request Body (JSON):

{
  "question": "What is LangGraph?"
}


Response (JSON):

{
  "answer": "LangGraph is a framework for building multi-agent workflows using graphs."
}

🧪 Testing

Open Swagger UI

Select POST /query

Click Try it out

Enter a question

Click Execute

View the response

🚀 Features

Multi-agent orchestration using LangGraph

FastAPI-based REST API

Modular and extensible agent design

Interactive API documentation with Swagger

🔮 Future Enhancements

Add memory support for agents

Integrate vector databases

Add authentication & authorization

Build a UI dashboard

👨‍💻 Author

K.V. Pratham
B.Tech – Information Technology

GitHub:
https://github.com/kvpratham8686-hue

📤 Submission Notes

This repository includes:

Complete source code

Clean README documentation

Setup and run instructions

API documentation via Swagger UI

The project is ready for evaluation and deployment.
