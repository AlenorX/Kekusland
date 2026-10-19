import asyncio
from fastapi import FastAPI, Response, Header
from src.api.router_fact import router

app = FastAPI(title="Facts-service")
app.include_router(router)

@app.get('/ping')
async def ping():
    return {"message": "Ok"}