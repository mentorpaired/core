import json
import unittest
from unittest.mock import patch

from rest_framework.test import APIClient


class TestGithubOauth(unittest.TestCase):
    def setUp(self):
        self.client = APIClient()

    @patch('app.views.github_oauth.get_user_from_token')
    @patch('app.views.github_oauth.convert_to_auth_token')
    @patch('app.views.github_oauth.retrieve_github_user_info')
    @patch('app.views.github_oauth.generate_github_access_token')
    def test_github_authenticate(self, generate_access_token,
                                 retrieve_github_user, convert_to_auth_token,
                                 get_user_from_token):
        generate_access_token.return_value = 'token'
        github_user = {'user_id': 'id1', 'avatar': 'avatar.jpg'}
        convert_to_auth_token.return_value = 'auth_token'
        retrieve_github_user.return_value = json.dumps(github_user)
        get_user_from_token.return_value = {'id': 1, 'username': 'name',
                                            'email': 'user@user.com'}

        mock_data = {
            'client_id': 'somerandomstring',
            'client_secret': 'anotherlongerrandomstring',
            'code': 'arandomstring01'
        }

        response = self.client.post('/github_auth/', data=mock_data)
        assert response.status_code == 201
        assert json.loads(response.content) == {
            'token': 'auth_token',
            'github_user_info': '{"user_id": "id1", "avatar": "avatar.jpg"}',
            'user': {'id': 1, 'username': 'name', 'email': 'user@user.com'}
        }
