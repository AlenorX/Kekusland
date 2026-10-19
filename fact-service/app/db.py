import json
import os
import random
from util import YAML
from sqlalchemy import select, insert, JSON
from sqlalchemy.orm import Mapped, DeclarativeBase, mapped_column
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine 

util = YAML()
source = util.decode('yaml/config.yml')
dict_config = source['configuration']
path_data = dict_config['PATH_DATA']

class Base(DeclarativeBase):
    pass

class Facts(Base):
    __tablename__ = "facts_api"
    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[list] = mapped_column(JSON)

connect = create_async_engine(f'sqlite+aiosqlite:///{dict_config['PATH_DATABASE']}')

async def init_models():
    async with connect.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("Таблицы успешно проверены/созданы!")

async def initialization_data():
    content = {}
    await init_models()
    if os.path.exists(path_data):
        with open(path_data, 'r+') as file:
            content = json.load(file)
    
    async with AsyncSession(connect) as session:
        async with session.begin():
            facts = Facts(text=content['text'])
            session.add(facts)

async def test():
    async with AsyncSession(connect) as session:
        async with session.begin():
            stmt = select(Facts.text)
            input_data = await session.scalars(stmt)
            facts = input_data.all()
            return random.choice(facts[0])

async def select_fact():
    if os.path.exists(dict_config['PATH_DATABASE']) == False:
        await initialization_data()
        return await test()
    else:
        return await test()
