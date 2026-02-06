# LangGraph Multi-Agent Knowledge Bot

## 📌 Project Overview

This project is a **LangGraph-based Multi-Agent Knowledge Bot** built using **Python** and **FastAPI**.  
It demonstrates how multiple AI agents can collaboratively process a user query and generate intelligent responses using a graph-based workflow.

The application exposes a REST API that allows users to submit questions and receive AI-generated responses.

---

## 📂 Project Structure

```text
langgraph-multi-agent-knowledge-bot/
├── api/
│   ├── main.py              # FastAPI application entry point
│   ├── graph/
│   │   └── agent_graph.py   # LangGraph workflow definition
│   └── agents/              # Agent logic (extendable)
├── requirements.txt         # Project dependencies
├── README.md                # Project documentation
└── .gitignore
