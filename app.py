import os
import sqlite3
from flask import Flask
from database import Base
from handlers.routes import configure_routes
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URI='postgresql://postgres:postgres@db:5432/postgres'

def create_app(session):
    app = Flask(__name__)
#    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['DB_SESSION'] = session
    return app

def create_db_session():
    # Crear un motor que almacena los datos en la base de datos SQLite local llamada "users.db"
    engine = create_engine('sqlite:///users.db')

    # Crear todas las tablas en la base de datos
    Base.metadata.create_all(engine)

    Session = sessionmaker()
    Session.configure(bind=engine)

    # Crear una nueva sesión
    session = Session()
    return session

session = create_db_session()
app = create_app(session)
configure_routes(app)

if __name__ == '__main__':
    app.run()
