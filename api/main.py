import sys
import os

# Add project root to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi import FastAPI
from pydantic import BaseModel

# Import LangGraph app
from graph.agent_graph import app as langgraph_app


class QueryRequest(BaseModel):
    query: str


# IMPORTANT: variable name MUST be `app`
app = FastAPI(title="LangGraph Multi-Agent API")


@app.post("/query")
async def query_agent(request: QueryRequest):
    result = langgraph_app.invoke({"query": request.query})
    return {"response": result}
