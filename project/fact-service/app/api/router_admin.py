import asyncio
import db as db
import exception as exception
import logging
from model.new_fact import NewFact
from fastapi import APIRouter, Header, Response, status

router = APIRouter(prefix='/admin')
secret_key = "test2020"
logging.basicConfig( level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")

@router.post('/add')
async def add_fact(resp: Response, schema: NewFact , x_api_key: str = Header()):
    try:
        if x_api_key == secret_key:
            asyncio.create_task(db.insert_fact(schema.text))
            resp.status_code = status.HTTP_201_CREATED
            return {"status": True, "message": "Success"}
        else:
            resp.status_code = status.HTTP_403_FORBIDDEN
            return {"status": False, "message": "Forbidden"}
    except exception.DataBaseError:
        logging.exception("Error database")
        resp.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"status": False, "message": "Internal database error"}
    except Exception:
        logging.exception("Error microservice")
        resp.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"status": False, "message": "Internal server error"}