import datetime
from sqlalchemy import (
    Column,
    Integer,
    Unicode,
    UnicodeText,
    DateTime
    )

from .meta import Base
from webhelpers2.text import urlify
from webhelpers2.date import distance_of_time_in_words


class BlogPost(Base):
    __tablename__ = 'BlogPost'
    id = Column(Integer, primary_key=True)
    title = Column(Unicode(255), unique=True, nullable=False)
    body = Column(UnicodeText, default=u'')
    created = Column(DateTime, default=datetime.datetime.utcnow)
    edited = Column(DateTime, default=datetime.datetime.utcnow)

    @property
    def slug(self):
        return urlify(self.title)

