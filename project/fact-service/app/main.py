import asyncio
from fastapi import FastAPI, Response, Header
from api.router_fact import router as router_fact
from api.router_admin import router as router_admin

app = FastAPI(title="Facts-service")
app.include_router(router_fact)
app.include_router(router_admin)

@app.get('/ping')
async def ping():
    return {"message": "Ok"}