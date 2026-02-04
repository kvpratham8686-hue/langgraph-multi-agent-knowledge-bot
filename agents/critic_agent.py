from langchain_openai import ChatOpenAI
from agents.prompts import CRITIC_PROMPT

llm = ChatOpenAI(temperature=0)

def critic_agent(state):
    response = llm.invoke(CRITIC_PROMPT + state["draft"])
    return {"review": response.content}
