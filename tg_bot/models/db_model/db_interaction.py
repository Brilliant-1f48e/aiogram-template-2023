import datetime

from sqlalchemy.orm import sessionmaker
from sqlalchemy import or_, and_

from tg_bot.models.db_model.db_client import DBClient


class DBInteraction(DBClient):
    def __init__(self, sqlalchemy_url: str, base):
        super().__init__(sqlalchemy_url, base)
        self.connect = sessionmaker(bind=self.engine)
        self.session = self.connect()

    async def add_customers(self) -> None:
        pass
