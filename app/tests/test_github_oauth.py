import json
import unittest
from unittest.mock import patch

from rest_framework.test import APIClient


class TestGithubOauth(unittest.TestCase):
    def setUp(self):
        self.client = APIClient()

    @patch("app.views.github_oauth.retrieve_github_user_info")
    @patch("app.views.github_oauth.generate_github_access_token")
    @patch("app.views.github_oauth.get_refresh_access_token")
    def test_github_authenticate(
        self,
        get_refresh_access_token,
        generate_access_token,
        retrieve_github_user,
    ):

        get_refresh_access_token.return_value = {
            "refresh": "randomrefreshtoken",
            "access": "randomaccesstoken",
        }

        generate_access_token.return_value = "token"

        github_user = {
            "user_id": "id1",
            "name": "test",
            "avatar_url": "https://dummyavatar.com/v0",
            "email": "test@test.com",
            "location": "CEST",
        }

        retrieve_github_user.return_value = github_user

        mock_data = {
            "client_id": "somerandomstring",
            "client_secret": "anotherlongerrandomstring",
            "code": "arandomstring01",
        }

        byte_response = self.client.post("/github_auth/", data=mock_data)
        assert byte_response.status_code == 201

        content = json.loads(byte_response.content)

        user = content.get("user")
        assert user is not None, "user not created"

        expected_response = {
            "jwt": {"refresh": "randomrefreshtoken", "access": "randomaccesstoken"},
            "github_user_info": {
                "user_id": "id1",
                "name": "test",
                "avatar_url": "https://dummyavatar.com/v0",
                "email": "test@test.com",
                "location": "CEST",
            },
            "user": {
                "user_id": user.get("user_id"),
                "username": "test",
                "email": "test@test.com",
                "role": [],
                "about": "",
                "avatar": "https://dummyavatar.com/v0",
                "skills": [],
                "pronoun": None,
                "spoken_languages": [],
                "timezone": "CEST",
                "availability": True,
            },
        }
        assert content == expected_response

        get_refresh_access_token.assert_called()
        generate_access_token.assert_called()
        retrieve_github_user.assert_called()
