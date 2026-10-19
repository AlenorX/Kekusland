import asyncio
from fastapi import FastAPI, Response, Header
from pydantic import BaseModel


app = FastAPI(title="Facts-service")



@app.get('/ping')
async def ping():
    return {"message": "Ok"}

@app.get('/facts/cat')
async def facts(resp: Response):
    # to-do реализовать работу отправки интересных фактов про котов
    pass