"""
Requests view
"""
from django.http import Http404
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from ..models import Request
from ..serializers import RequestSerializer


class RequestList(APIView):
    """
    Requests
        :param APIView: Wrapper for class-based views
    """

    permission_classes = (IsAuthenticated,)

    def get(self, request: Request) -> Response:
        """
        Get all requests
            :param request: Request object
            :return: All requests
        """
        request = Request.objects.all()
        serializer = RequestSerializer(request, many=True)
        return Response(serializer.data)

    def post(self, request: Request) -> Response:
        """
        Create request
            :param request: Request object
            :return: New request or error
        """
        serializer = RequestSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RequestDetail(APIView):
    """
    Request details
        :param APIView: Wrapper for class-based views
    """

    permission_classes = (IsAuthenticated,)

    def get_object(self, primary_key: str) -> Request:
        """
        Get single request
            :param primary_key: request primary key
            :return: request
        """
        try:
            return Request.objects.get(id=primary_key)
        except Request.DoesNotExist as err:
            raise Http404 from err

    def get(self, request: Request, primary_key: str) -> Response:
        """
        Get single request
            :param request: Request object
            :param primary_key: request primary key
            :return: single request object
        """
        request = self.get_object(primary_key)
        serializer = RequestSerializer(request)
        return Response(serializer.data)

    def put(self, request: Request, primary_key: str) -> Response:
        """
        Update single request
            :param request: Request object
            :param primary_key: request primary key
            :return: single request object
        """
        request_obj = self.get_object(primary_key)
        serializer = RequestSerializer(request_obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, primary_key: str) -> Response:
        """
        Delete single request
            :param request: Request object
            :param primary_key: request primary key
            :return: single request object
        """
        request = self.get_object(primary_key)
        request.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
