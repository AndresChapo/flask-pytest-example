
from sqlalchemy import Column, Integer, String
from database import Base, Database


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
        db = Database()
        db.session.add(u)
        db.session.commit()
        return u
    
    @staticmethod
    def get_users_list():
        db = Database()
        return db.session.query(User).all()