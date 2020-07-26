import os
import requests

from dotenv import load_dotenv
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..oauth import generate_github_access_token
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
        print('=====>', request.data)
        github_token = generate_github_access_token(
            github_client_id=SOCIAL_AUTH_GITHUB_KEY,
            github_client_secret=SOCIAL_AUTH_GITHUB_SECRET,
            github_code=request.data['code']
        )

        return Response(
            {
                'token': github_token,
                # 'user': GithubAuthSerializer(github_user).data
            },
            status=status.HTTP_201_CREATED
        )


class GithubUser(APIView):
    def get(self, request):
        # github_token = request.query_params['token']
        user_data = requests.get(
            'https://api.github.com/user',
            headers={'Authorization': 'token ' + github_token,
                     'content-type': 'application/json'})

        return user_data
