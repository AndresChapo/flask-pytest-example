from flask import Blueprint, request
import json
from models.users_model import User

example_endpoints_blueprint = Blueprint("example_endpoints", __name__)

@example_endpoints_blueprint.route('/ping')
def ping():
    return 'pong'

@example_endpoints_blueprint.route('/')
def hello_world():
    return 'Hello, World!'

@example_endpoints_blueprint.route('/post/test', methods=['POST'])
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

@example_endpoints_blueprint.route('/create_user', methods=['POST'])
def create_user():
    data_string = request.get_data()
    data = json.loads(data_string)

    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    if name and email and password:
        u = User().create(name, email, password)
        return {'id': u.id, 'name': u.name, 'email': u.email}, 200
    else:
        return 'Bad Request', 400

@example_endpoints_blueprint.route('/users')
def get_users():
    users = User().get_users_list()
    # Convert query results into a list of dictionaries
    response = [{'id': u.id, 'name': u.name, 'email': u.email} for u in users]

    return response, 200
