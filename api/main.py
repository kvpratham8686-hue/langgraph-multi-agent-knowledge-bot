import sys
import os

# ✅ Add project root to Python path so langgraph can be found
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi import FastAPI
from pydantic import BaseModel

# Import LangGraph app
from graph.agent_graph import app as langgraph_app


class QueryRequest(BaseModel):
    query: str


api = FastAPI(title="LangGraph Multi-Agent API")


@api.post("/query")
async def query_agent(request: QueryRequest):
    result = langgraph_app.invoke({"query": request.query})
    return {"response": result}
