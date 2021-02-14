import datetime
import logging

from rest_framework import exceptions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from ..github_oauth import (
    generate_github_access_token,
    retrieve_github_user_email,
    retrieve_github_user_info,
)
from ..models import User
from ..serializers import UserSerializer


def get_refresh_access_token(user_object):
    refresh = RefreshToken.for_user(user_object)
    access_token = refresh.access_token
    access_token.set_exp(lifetime=datetime.timedelta(minutes=480))
    return {"refresh": str(refresh), "access": str(access_token)}


@api_view(["POST"])
def github_authenticate(request):
    github_token = generate_github_access_token(
        github_code=request.data["code"],
    )

    github_user = retrieve_github_user_info(token=github_token)

    email = github_user.get("email")

    if email is None:

        """
        github_private_email is a list containing two dictionaries,
        each one with different emails. According to github's private email current setup,
        the first dictionary values contains the primary and verified email value.
        """

        github_private_email = retrieve_github_user_email(token=github_token)
        retrieved_private_email = github_private_email[0]
        email = retrieved_private_email.get("email")

    github_user_name = github_user.get("name")

    try:
        user = User.objects.get(email=github_user.get("email"))
    except User.DoesNotExist:
        user, created = User.objects.get_or_create(
            username=github_user.get("name"),
            avatar=github_user.get("avatar_url"),
            email=email,
            timezone=github_user.get("location"),
        )

    if user is None:
        logging.error(f"Github account for {github_user_name} was not created.")
        raise exceptions.AuthenticationFailed("user not created")

    res = get_refresh_access_token(user)

    return Response(
        {
            "jwt": res,
            "github_user_info": github_user,
            "user": UserSerializer(user).data,
        },
        status=status.HTTP_201_CREATED,
    )
