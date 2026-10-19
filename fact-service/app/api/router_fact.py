import requests
import exception
import schema.cats as schema
import db
import json
from util import YAML
from fastapi import APIRouter, Response, status

router = APIRouter(prefix='/fact')
util = YAML()
dict_config = util.decode('yaml/config.yml')
webhook_url = dict_config['configuration']

@router.get('/cat')
async def facts_cat(resp: Response):
    try:
        response_webhook = requests.get(
            webhook_url['WEBHOOK_URL']['cat-fact']
        )
        payload = json.loads(response_webhook.content)
        model = schema.Cats(**payload) # validate input data from Public API (https://catfact.ninja)
        return {"status": True, "fact": model.fact}
    except requests.exceptions.ConnectTimeout:
        resp.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"status": False, "message": "Connect timeout :("}

@router.get('/api')
async def facts_api(resp: Response):
    try:
        result = await db.select_fact()
        if result:
            return {"status": True, "fact": result}
        else:
            raise exception.FactsNotFound("Facts not found")
    except exception.FactsNotFound:
        resp.status_code = status.HTTP_409_CONFLICT
        return {"status": False, "message": "Facts not found"}
