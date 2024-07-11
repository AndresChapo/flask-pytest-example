import json

class TestRoutes:
    """ Examples using pytest fixtures """

    def test_ping(self, api_client):
        """ Example using pytest fixtures """

        url = '/ping'        
        response = api_client.get(url)
        assert response.get_data() == b'pong'
        assert response.status_code == 200

    def test_post_route__success(self, app):
        client = app.test_client()
        url = '/post/test'

        mock_request_headers = [(
            'authorization-sha256', '123'
        )]

        mock_request_data = {
            'request_id': '123',
            'payload': {
                'py': 'pi',
                'java': 'script'
            }
        }


        response = client.post(url, data=json.dumps(mock_request_data), headers=mock_request_headers)
        assert response.status_code == 200

    def test_post_route__success_2(self, api_client):
        url = '/post/test'

        mock_request_headers = [(
            'authorization-sha256', '123'
        )]

        mock_request_data = {
            'request_id': '123',
            'payload': {
                'py': 'pi',
                'java': 'script'
            }
        }

        response = api_client.post(url, data=mock_request_data, headers=mock_request_headers)
        assert response.status_code == 200


    def test_post_route__failure__unauthorized(self, app):
        client = app.test_client()
        url = '/post/test'

        mock_request_headers = {}

        mock_request_data = {
            'request_id': '123',
            'payload': {
                'py': 'pi',
                'java': 'script'
            }
        }

        response = client.post(url, data=json.dumps(mock_request_data), headers=mock_request_headers)
        assert response.status_code == 401


    def test_post_route__failure__bad_request(self, app):
        client = app.test_client()
        url = '/post/test'

        mock_request_headers = {
            'authorization-sha256': '123'
        }

        mock_request_data = {}

        response = client.post(url, data=json.dumps(mock_request_data), headers=mock_request_headers)
        assert response.status_code == 400
