import json
import os
import random
from src.util import YAML
from sqlalchemy import create_engine, select, insert, JSON
from sqlalchemy.orm import Mapped, DeclarativeBase, mapped_column
from sqlalchemy.ext.asyncio import AsyncSession 

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

connect = create_engine(f'sqlite:///{dict_config['PATH_DATABASE']}')

async def initialization_data() -> bool:
    content = {}
    if os.path.exists(path_data):
        with open(path_data, 'r+') as file:
            content = json.load(file)
    else:
        async with AsyncSession(connect) as session:
            with session.begin():
                facts = Facts(text=content['text'])
                session.add(facts)

async def select_fact():
    if os.path.exists(dict_config['PATH_DATABASE']):
        async with AsyncSession(connect) as session:
                with session.begin():
                    stmt = select(Facts)
                    input_data = await session.scalars(stmt)
                    facts = input_data.all()
                    count = random.randint(0, len(facts))
                    return facts[count]
    else:
        await initialization_data()

