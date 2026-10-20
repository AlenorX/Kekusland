import random
from util import YAML
from sqlalchemy import select, insert, ARRAY, String
from sqlalchemy.orm import Mapped, DeclarativeBase, mapped_column
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine 

util = YAML()
source = util.decode('yaml/config.yml')
dict_config = source['configuration']

class Base(DeclarativeBase):
    pass

class Facts(Base):
    __tablename__ = dict_config['DATABASE']['NAME_TABLE']
    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[list] = mapped_column(ARRAY(String))

connect = create_async_engine(f'postgresql+asyncpg://{dict_config['DATABASE']['USERNAME']}:{dict_config['DATABASE']['PASSWORD']}@{dict_config['DATABASE']['NAME_CONTAINER']}:{dict_config['DATABASE']['PORT']}/{dict_config['DATABASE']['NAME_DATABASE']}')

async def select_fact():
    async with AsyncSession(connect) as session:
        async with session.begin():
            stmt = select(Facts.text)
            input_data = await session.scalars(stmt)
            facts = input_data.all()
            return random.choice(facts[0])
