from flask import app
from sqlalchemy import Column, Integer, String
from database import Base, session


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    @staticmethod
    def create(name, email, password):
        u = User(name=name, email=email, password=password)
        u.name = name
        u.email = email
        u.password = password

        session.add(u)
        session.commit()
        return u
    