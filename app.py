from flask import Flask
#from database import db_session

DATABASE_URI='sqlite:///users.db'


def register_blueprints(app):
    """Register blueprint endpoints"""

    from handlers.routes import example_endpoints_blueprint

    app.register_blueprint(example_endpoints_blueprint)

def register_env_vars(app):
    app.config['DATABASE_URI'] = DATABASE_URI
#    app.config['DB_SESSION'] = db_session

def create_app():
    app = Flask(__name__)
    register_blueprints(app)
    return app

app = create_app()

register_env_vars(app)

if __name__ == '__main__':
    app.run()
