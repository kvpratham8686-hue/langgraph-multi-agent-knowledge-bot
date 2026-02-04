import sys
import os

# ✅ Add project root to Python path so langgraph can be found
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from typing import TypedDict
from langgraph.graph import StateGraph, END


# -------------------------
# Define the state
# -------------------------
class AgentState(TypedDict):
    query: str
    response: str


# -------------------------
# Define agent function
# -------------------------
def simple_agent(state: AgentState) -> AgentState:
    user_query = state["query"]

    # Simple response logic (can be replaced with LLM later)
    response = f"LangGraph is a framework for building multi-agent workflows using graphs. Your question was: {user_query}"

    return {
        "query": user_query,
        "response": response
    }


# -------------------------
# Build LangGraph
# -------------------------
graph = StateGraph(AgentState)

graph.add_node("agent", simple_agent)
graph.set_entry_point("agent")
graph.add_edge("agent", END)

app = graph.compile()
