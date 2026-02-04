from langchain_openai import ChatOpenAI
from agents.prompts import KNOWLEDGE_PROMPT

llm = ChatOpenAI(temperature=0)

def knowledge_agent(state):
    memory = state.get("memory", "")
    response = llm.invoke(KNOWLEDGE_PROMPT + memory)
    return {"knowledge": response.content}
