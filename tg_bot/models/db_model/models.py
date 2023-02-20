import datetime

from sqlalchemy import Column, Integer, String, Date, ForeignKey, Boolean, BigInteger, TIMESTAMP

from tg_bot.models.db_model import Base


class User(Base):
    __tablename__ = "users"

    id = Column(BigInteger, nullable=False, unique=True, primary_key=True, autoincrement=True)
    chat_id = Column(BigInteger, nullable=False, unique=True)
