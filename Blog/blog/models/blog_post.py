import datetime
from sqlalchemy import (
    Column,
    Integer,
    Unicode,
    UnicodeText,
    DateTime
    )

from .meta import Base


class BlogPost(Base):
    __tablename__ = 'BlogPost'
    id = Column(Integer, primary_key=True)
    title = Column(Unicode(255), unique=True, nullable=False)
    body = Column(UnicodeText, default=u'')
    created = Column(DateTime, default=datetime.datetime.utcnow)
    edited = Column(DateTime, default=datetime.datetime.utcnow)


