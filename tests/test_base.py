from app import create_app

def test_base_route_raw():
        """ Example without using pytest fixtures """
        app = create_app(None)
        app.config["TESTING"] = True
        client = app.test_client()
        url = '/'

        response = client.get(url)
        assert response.get_data() == b'Hello, World!'
        assert response.status_code == 200
