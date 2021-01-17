import datetime

from rest_framework import status, exceptions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from ..gitlab_oauth import generate_gitlab_access_token, retrieve_gitlab_user_info
from ..models import User
from ..serializers import UserSerializer


def get_refresh_access_token(user_object):
    refresh = RefreshToken.for_user(user_object)
    access_token = refresh.access_token
    access_token.set_exp(lifetime=datetime.timedelta(minutes=480))
    return {"refresh": str(refresh), "access": str(access_token)}


@api_view(["POST"])
def gitlab_authenticate(request):

    gitlab_token = generate_gitlab_access_token(
        code=request.data["code"],
        grant_type="authorization_code",
        redirect_uri="http://localhost:3000/login",
    )

    gitlab_user = retrieve_gitlab_user_info(access_token=gitlab_token)

    try:
        user = User.objects.get(email=gitlab_user.get("email"))
    except User.DoesNotExist:
        user, created = User.objects.get_or_create(
            username=gitlab_user.get("name"),
            avatar=gitlab_user.get("avatar_url"),
            email=gitlab_user.get("email"),
        )

    if user is None:
        raise exceptions.AuthenticationFailed("user not created")

    res = get_refresh_access_token(user)

    return Response(
        {
            "jwt": res,
            "gitlab_user_info": gitlab_user,
            "user": UserSerializer(user).data,
        },
        status=status.HTTP_201_CREATED,
    )