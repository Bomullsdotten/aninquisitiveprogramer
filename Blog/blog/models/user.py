import datetime
from sqlalchemy import (
    Column,
    Integer,
    Unicode,
    UnicodeText,
    DateTime
    )

from .meta import Base


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(255), unique=True, nullable=False)
    password = Column(Unicode(255), nullable=False)
    last_logged = Column(DateTime, default=datetime.datetime.utcnow)


