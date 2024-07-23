
from base import create_app, register_env_vars
from database import Database

DATABASE_URI='sqlite:///users.db'

db = Database(DATABASE_URI)
app = create_app()

register_env_vars(app)

if __name__ == '__main__':
    app.run()
