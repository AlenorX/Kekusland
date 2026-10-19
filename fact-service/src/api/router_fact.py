import requests
import src.schema.cats as schema
from src.util import YAML
from fastapi import APIRouter, Response, status

router = APIRouter(prefix='/fact')
util = YAML()
dict_config = util.decode('yaml/config.yml')
webhook_url = dict_config['configuration']

@router.get('/cat')
async def facts_cat(resp: Response):
    try:
        response_webhook = requests.get(
            webhook_url['WEBHOOK_URL']
        )
        model = schema.Cats(**response_webhook) # validate input data from Public API (https://catfact.ninja)
        return {"status": True, "fact": model.fact}
    except requests.exceptions.ConnectTimeout:
        resp.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"status": False, "message": "Connect timeout :("}