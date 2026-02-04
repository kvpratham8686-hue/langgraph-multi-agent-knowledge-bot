from langchain_openai import ChatOpenAI
from agents.prompts import PLANNER_PROMPT

llm = ChatOpenAI(temperature=0)

def planner_agent(state):
    response = llm.invoke(PLANNER_PROMPT + state["query"])
    return {"plan": response.content}
