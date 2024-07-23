from flask import Flask

DATABASE_URI='sqlite:///users.db'

def register_blueprints(app):
    """Register blueprint endpoints"""

    from handlers.routes import example_endpoints_blueprint

    app.register_blueprint(example_endpoints_blueprint)

def register_env_vars(app):
    app.config['DATABASE_URI'] = DATABASE_URI

def create_app():
    app = Flask(__name__)
    register_blueprints(app)
    return app
