
class TestRoutes:
    """ Examples using pytest fixtures """

    def test_ping(self, api_client):
        """ Example using pytest fixtures """

        url = '/ping'        
        response = api_client.get(url)
        assert response.get_data() == b'pong'
        assert response.status_code == 200

    def test_post_route__success(self, api_client):
        """Test post/test happy path"""
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

    def test_post_route__failure__unauthorized(self, api_client):
        """Run post/test without auth"""

        url = '/post/test'

        mock_request_headers = [] # As we don't send the auth token it will fail

        mock_request_data = {
            'request_id': '123',
            'payload': {
                'py': 'pi',
                'java': 'script'
            }
        }

        response = api_client.post(url, data=mock_request_data, headers=mock_request_headers)
        assert response.status_code == 401

    def test_post_route__failure__bad_request(self, api_client):
        """Run post/test and provoke a bad request"""
        url = '/post/test'

        mock_request_headers = [(
            'authorization-sha256', '123'
        )]

        mock_request_data = {} # As we don't send the payload it will fail

        response = api_client.post(url, data=mock_request_data, headers=mock_request_headers)
        assert response.status_code == 400
