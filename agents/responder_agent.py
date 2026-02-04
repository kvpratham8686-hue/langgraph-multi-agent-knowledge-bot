from langchain_openai import ChatOpenAI
from agents.prompts import RESPONDER_PROMPT

llm = ChatOpenAI(temperature=0)

def responder_agent(state):
    combined = f"""
    {state.get('plan')}
    {state.get('research')}
    {state.get('knowledge')}
    {state.get('review')}
    """
    response = llm.invoke(RESPONDER_PROMPT + combined)
    return {"final_answer": response.content, "draft": response.content}
