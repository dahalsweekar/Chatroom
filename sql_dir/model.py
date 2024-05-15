from sqlalchemy import Column, Integer, String, ForeignKey
from .database import Base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String, index=True)
    lastname = Column(String)
    email = Column(String, index=True)
    phone = Column(Integer, unique=True)
    password = Column(String)

    def __repr__(self):
        return f"<User {self.username}"
