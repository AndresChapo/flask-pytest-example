from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URI ='sqlite:///users.db' # Valor por defecto
Base = declarative_base()

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
