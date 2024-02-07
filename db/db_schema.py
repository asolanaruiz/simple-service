from sqlalchemy import Column, Integer, String
from db.db import Base


class DBUser(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String)
    password = Column(String)
    token = Column(String)
