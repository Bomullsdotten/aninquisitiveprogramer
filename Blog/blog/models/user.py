from passlib.apps import custom_app_context as pwd_context


def hash_password(pwd):
    return pwd_context.encrypt(pwd, category='admin')


def check_password(pwd, expected_hash):
    return pwd_context.verify(pwd, expected_hash)




import datetime
from sqlalchemy import (
    Column,
    Integer,
    UnicodeText,
    DateTime,
    Text
    )

from .meta import Base


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(UnicodeText(255), unique=True, nullable=False)
    password_hash = Column(UnicodeText(255))
    role = Column(Text, nullable=False)
    last_logged = Column(DateTime, default=datetime.datetime.utcnow)

    def set_password(self, pwd):
        pwd_hash = pwd_context.encrypt(pwd, category='admin')
        self.password_hash = pwd_hash

    def check_password(self, pwd):
        if self.password_hash is not None:
            expected_hash = self.password_hash
            return pwd_context.verify(pwd, expected_hash)

        return False
