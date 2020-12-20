import json
import unittest
from unittest.mock import patch

from rest_framework.test import APIClient


class TestGitlabOauth(unittest.TestCase):
    def setUp(self):
        self.client = APIClient()

    @patch("app.views.gitlab_oauth.retrieve_gitlab_user_info")
    @patch("app.views.gitlab_oauth.generate_gitlab_access_token")
    @patch("app.views.gitlab_oauth.get_refresh_access_token")
    def test_gitlab_authenticate(
        self,
        get_refresh_access_token,
        generate_gitlab_access_token,
        retrieve_gitlab_user_info,
    ):

        get_refresh_access_token.return_value = {
            "refresh": "randomrefreshtoken",
            "access": "randomaccesstoken",
        }

        generate_gitlab_access_token.return_value = "token"

        gitlab_user = {
            "id": "id0",
            "name": "gitlab_test",
            "avatar_url": "https://secure.gravatar.com/avatar/v0",
            "email": "gitlabtest@test.com",
        }

        retrieve_gitlab_user_info.return_value = gitlab_user

        mock_data = {
            "client_id": "somerandomstring",
            "client_secret": "anotherrandomstring",
            "code": "arandomstring00",
            "grant_type": "dummy_grant_type",
            "redirect_uri": "http://test:3000/testing",
        }

        response = self.client.post("/gitlab_auth/", data=mock_data)
        assert response.status_code == 201

        content = json.loads(response.content)

        user = content.get("user")
        assert user is not None, "user not created"

        expected_response = {
            "jwt": {"refresh": "randomrefreshtoken", "access": "randomaccesstoken"},
            "gitlab_user_info": {
                "id": "id0",
                "name": "gitlab_test",
                "avatar_url": "https://secure.gravatar.com/avatar/v0",
                "email": "gitlabtest@test.com",
            },
            "user": {
                "user_id": user.get("user_id"),
                "username": "gitlab_test",
                "email": "gitlabtest@test.com",
                "role": [],
                "about": "",
                "avatar": "https://secure.gravatar.com/avatar/v0",
                "skills": [],
                "pronoun": None,
                "spoken_languages": [],
                "timezone": "",
                "availability": True,
            },
        }
        assert content == expected_response

        get_refresh_access_token.assert_called()
        generate_gitlab_access_token.assert_called()
        retrieve_gitlab_user_info.assert_called()
