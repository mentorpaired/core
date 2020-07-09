import json
import re

import requests
from oauth2_provider.models import AccessToken

from .models import GithubAuth


def generate_github_access_token(github_client_id, github_client_secret, github_code):
    """
    create an access token to github oauth2
    """
    github_response = requests.post(
        'https://github.com/login/oauth/access_token/',
        data=json.dumps({
            'client_id': github_client_id,
            'client_secret': github_client_secret,
            'code': github_code
        }),
        headers={'content-type': 'application/json'}
    )

    token = re.search(r'access_token=([a-zA-Z0-9]+)',
                      github_response.content.decode('utf-8'))
    if token is None:
        raise PermissionError(github_response)
    print(token.group(1))
    return token.group(1)


def convert_to_auth_token(client_id, client_secret, backend, token):
    """
    using the previously generated access_token, use the
    django-rest-framework-social-oauth2 endpoint `/convert-token/` to
    authenticate the user and return a django auth token
    """
    data = {
        'grant_type': 'convert_token',
        'client_id': client_id,
        'client_secret': client_secret,
        'backend': backend,
        'token': token,
    }
    response = requests.post('http://127.0.0.1:8000/auth/convert-token/', data=data)
    return response.json()


def get_user_from_token(django_auth_token):
    """
    Retrieve user from access token
    """
    return GithubAuth.objects.get(
        github_user_id=AccessToken.objects.get(token=django_auth_token['access_token']).user_id
    )
