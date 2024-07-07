from flask import current_app, request
import json

from models.users_model import User


def configure_routes(app):

    @app.route('/')
    def hello_world():
        return 'Hello, World!'

    @app.route('/post/test', methods=['POST'])
    def receive_post():
        headers = request.headers

        auth_token = headers.get('authorization-sha256')
        if not auth_token:
            return 'Unauthorized', 401

        data_string = request.get_data()
        data = json.loads(data_string)

        request_id = data.get('request_id')
        payload = data.get('payload')

        if request_id and payload:
            return 'Ok', 200
        else:
            return 'Bad Request', 400

    @app.route('/create_user')
    def create_users():
        user = User()
        user.name = 'juan'
        user.email = 'juan@email.com'

        # Save user in the database
        session = current_app.config['DB_SESSION']
        session.add(user)
        session.commit()
        return user.name

    @app.route('/users')
    def get_users():
        session = current_app.config['DB_SESSION']
        users = session.query(User).all()
        # Convert query results into a list of dictionaries
        response = [{'id': u.id, 'name': u.name, 'email': u.email} for u in users]

        return response, 200
