"""
User view
"""
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from ..models import User
from ..serializers import UserSerializer


class UserList(APIView):
    """
    Users
        :param APIView:
    """

    permission_classes = (IsAuthenticated,)

    def get(self, request: User) -> Response:
        """
        Get all users
            :param user: User object
            :return: All users
        """
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request: User) -> Response:
        """
        Create user
            :param user: User object
            :return: New user or error
        """
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk: str) -> User:
        """
        Get single user
            :param pk: user primary key
            :return: user
        """
        try:
            return User.objects.get(user_id=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request: User, pk: str) -> Response:
        """
        Get single user
            :param user: User object
            :param pk: user primary key
            :return: single user object
        """
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request: User, pk: str) -> Response:
        """
        Update single user
            :param user: User object
            :param pk: user primary key
            :return: single user object
        """
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: User, pk: str) -> Response:
        """
        Delete single user
            :param user: User object
            :param pk: user primary key
            :return: single user object
        """
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
