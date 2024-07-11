import os
import sqlite3
from flask import Flask
from database import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#SQLALCHEMY_DATABASE_URI='postgresql://postgres:postgres@db:5432/postgres'
DATABASE_URI='sqlite:///users.db'
TEST_DATABASE_URI='sqlite:///test_users.db'

def register_blueprints(app):
    """Register blueprint endpoints"""

    from handlers.routes import example_endpoints_blueprint

    app.register_blueprint(example_endpoints_blueprint)


def create_app(session):
    app = Flask(__name__)
    app.config['DATABASE_URI'] = DATABASE_URI
    app.config['DB_SESSION'] = session
    register_blueprints(app)
    return app

def create_db_session(database_uri):
    # Crear un motor que almacena los datos en la base de datos SQLite local llamada "users.db"
    engine = create_engine(database_uri)

    # Crear todas las tablas en la base de datos
    Base.metadata.create_all(engine)

    Session = sessionmaker()
    Session.configure(bind=engine)

    # Crear una nueva sesión
    session = Session()
    return session

session = create_db_session(DATABASE_URI)
app = create_app(session)


if __name__ == '__main__':
    app.run()
