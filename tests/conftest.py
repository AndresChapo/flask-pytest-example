import json
from flask import session
import pytest
from app import create_app

class Constants:
    class HttpHeaders:
        AUTHORIZATION = 'Authorization'

access_token=''

@pytest.fixture(autouse=True)
def app():
    app = create_app(session)
    app.config["TESTING"] = True
    yield app

@pytest.fixture(autouse=True)
def client(app):
    yield app.test_client()

@pytest.fixture
def api_client(client):
    class ApiClient:
        def __init__(self):
            self.client = client

        def _check_headers(self, headers=None, authenticated=False):
            if not headers:
                headers = [("Accept", "application/json")]
            if authenticated:
                headers.append(
                    (Constants.HttpHeaders.AUTHORIZATION, "Bearer " + access_token)
                )
            return headers

        def post(self, url, data, headers=None, environ_base={}, authenticated=True):
            headers = self._check_headers(headers=headers, authenticated=authenticated)

            return self.client.post(
                url,
                data=json.dumps(data),
                content_type="application/json",
                headers=headers,
                environ_base=environ_base,
            )

        def post_form(self, url, data, headers, environ_base={}, authenticated=True):
            headers = self._check_headers(headers=headers, authenticated=authenticated)

            return self.client.post(
                url,
                data=data,
                content_type="application/x-www-form-urlencoded",
                headers=headers,
                environ_base=environ_base,
            )

        def post_form_file(
            self, url, data, headers, environ_base={}, authenticated=True
        ):
            headers = self._check_headers(headers=headers, authenticated=authenticated)

            return self.client.post(
                url,
                data=data,
                content_type="multipart/form-data",
                headers=headers,
                environ_base=environ_base,
            )

        def patch_form(self, url, data, headers, environ_base={}, authenticated=True):
            headers = self._check_headers(headers=headers, authenticated=authenticated)

            return self.client.patch(
                url,
                data=data,
                content_type="multipart/form-data",
                headers=headers,
                environ_base=environ_base,
            )

        def patch(self, url, data, headers=None):
            headers = self._check_headers(headers=headers)

            return self.client.patch(url, json=data, headers=headers)

        def get(
            self,
            url,
            headers=None,
            query_string=None,
            environ_base={},
            authenticated=True,
        ):
            headers = self._check_headers(headers=headers, authenticated=authenticated)

            return self.client.get(
                url,
                content_type="application/json",
                headers=headers,
                query_string=query_string,
                environ_base=environ_base,
            )

        def delete(self, url, data, headers=None):
            headers = self._check_headers(headers=headers)

            return self.client.delete(
                url,
                data=json.dumps(data),
                content_type="application/json",
                headers=headers,
            )

    return ApiClient()

