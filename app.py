from flask import Flask
from handlers.routes import configure_routes

def create_app():
    app = Flask(__name__)
    return app

app = create_app()
configure_routes(app)

if __name__ == '__main__':
    app.run()
