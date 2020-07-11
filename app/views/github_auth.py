import os

from dotenv import load_dotenv
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..oauth import (convert_to_auth_token, generate_github_access_token,
                     get_user_from_token)
from ..serializers import GithubAuthSerializer


load_dotenv()

# Github client id and client secret
SOCIAL_AUTH_GITHUB_KEY = os.getenv('SOCIAL_AUTH_GITHUB_KEY')
SOCIAL_AUTH_GITHUB_SECRET = os.getenv('SOCIAL_AUTH_GITHUB_SECRET')

# Oauth Toolkit id and secret
CLIENT_ID = os.getenv('DJANGO_OAUTH_APP_CLIENT_ID')
CLIENT_SECRET = os.getenv('DJANGO_OAUTH_APP_CLIENT_SECRET')


class GithubAuthView(APIView):

    def post(self, request):
        github_token = generate_github_access_token(
            github_client_id=SOCIAL_AUTH_GITHUB_KEY,
            github_client_secret=SOCIAL_AUTH_GITHUB_SECRET,
            github_code=request.data['code']
        )

        django_auth_token = convert_to_auth_token(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            backend='github',
            token=github_token
        )
        github_user = get_user_from_token(django_auth_token)

        return Response(
            {
                'token': django_auth_token,
                'user': GithubAuthSerializer(github_user).data
            },
            status=status.HTTP_201_CREATED
        )
