import json
import logging
import os
import re
import requests

from dotenv import load_dotenv

load_dotenv()


def generate_github_access_token(github_code):
    """
    create an access token to github Oauth2.
    :code: code generated by client from http://github.com/login/oauth/authorize/
    :return: json data on user's api
    """

    github_client_id = os.getenv("SOCIAL_AUTH_GITHUB_KEY")
    github_client_secret = os.getenv("SOCIAL_AUTH_GITHUB_SECRET")

    if not github_client_id or not github_client_secret:
        logging.critical("Github application client id or client secret is missing.")
        raise ValueError("Github application client id or client secret is missing.")

    github_response = requests.post(
        "https://github.com/login/oauth/access_token/",
        data=json.dumps(
            {
                "client_id": github_client_id,
                "client_secret": github_client_secret,
                "code": github_code,
            }
        ),
        headers={"content-type": "application/json"},
    )
    assert (
        github_response.status_code == 200
    ), f"ERROR: {github_response.status_code}, {github_response.text}"
    token = re.search(
        r"access_token=([a-zA-Z0-9]+)", github_response.content.decode("utf-8")
    )
    if not token:
        logging.warning("Wrong access token.")
        raise PermissionError(github_response)
    return token.group(1)


def retrieve_github_user_info(token):
    """
    using the access token returned by github, retrieve the user's info from the github api
    :token: access token generated from github
    """
    response = requests.get(
        "https://api.github.com/user",
        data={"token": token},
        headers={"Authorization": f"token {token}", "content-type": "application/json"},
    )
    return response.json()
