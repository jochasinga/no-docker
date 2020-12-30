from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get("/api/greet")
async def list_buckets(name: Optional[str] = None):
    if name is None:
        name = "John"
    return { "greeting": f"Hello, {name}!" }
