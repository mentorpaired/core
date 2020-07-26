import json
import re

import requests

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
    assert github_response.status_code == 200, \
        f'ERROR: {github_response.status_code}, {github_response.text}'
    token = re.search(r'access_token=([a-zA-Z0-9]+)',
                      github_response.content.decode('utf-8'))
    if not token:
        raise PermissionError(github_response)
    return token.group(1)


# def get_user_data_from_token(token):
#     """
#     using the previously generated access_token, retrieve the user data
#     """
#     response = requests.get(
#         'https://api.github.com/user',
#         headers={'Authorization': 'token ' + token, 'content-type': 'application/json'})

#     return response.json()
