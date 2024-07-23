from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base
#from app import DATABASE_URI
from models.singleton import Singleton

DATABASE_URI='sqlite:///users.db'
Base = declarative_base()

class Database(metaclass=Singleton):
    session = None
    connection = None
    trans = None

    def __init__(self, uri=None) -> None:
        print("BD: ", uri)
        engine = create_engine(uri, echo=False)
        self.session = scoped_session(sessionmaker(bind=engine, autocommit=False, autoflush=True))

        self.connection = engine.connect()
        self.trans = self.connection.begin()

        Base.metadata.create_all(bind=engine)

        
"""
def init_dbx(uri=None):
#    global engine
#    global db_session

    if uri:
        DATABASE_URI = uri

    engine = create_engine(DATABASE_URI, echo=False)
    db_session = scoped_session(sessionmaker(bind=engine, autocommit=False, autoflush=True))

    connection = engine.connect()
    trans = connection.begin()

    import models.users_model  # Importar todos los modelos aquí
    Base.metadata.create_all(bind=engine)

    return connection, trans


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

#db_session = create_db_session(DATABASE_URI)
db_session = init_db(DATABASE_URI)
"""