"""
Request Interests view
"""
from django.http import Http404
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import RequestInterest
from ..serializers import RequestInterestSerializer


# pylint: disable=unused-argument
class RequestInterestList(APIView):
    """
    Request Interests
        :param APIView: Wrapper for class-based views

        * Requires JWT authentication.
        * Only authenticated users are able to access this view
    """

    permission_classes = (IsAuthenticated,)

    def get(self, request: RequestInterest) -> Response:
        """
        Get all interests
            :param request: RequestInterest object
            :return: All request interests
        """
        interests = RequestInterest.objects.all()
        serializer = RequestInterestSerializer(interests, many=True)
        return Response(serializer.data)

    def post(self, request: RequestInterest) -> Response:
        """
        Create new interest
            :param request: Request Interest object
            :return: New interest or error
        """
        serializer = RequestInterestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# pylint: disable=unused-argument
class MentorRequestInterest(APIView):
    """
    Interest details from a specific request
        :param APIView: Wrapper for class-based views

        * Requires JWT authentication
        * Only authenticated users should be able to retrieve all their interests.
    """

    permission_classes = (IsAuthenticated,)

    def get_object(self, request_id: str) -> Response:
        """
        Extract request's primary key
            :param request_id: Request object primary key
            :return: primary key value for single Request
        """
        try:
            return RequestInterest.objects.filter(request_id__exact=request_id)
        except RequestInterest.DoesNotExist as err:
            raise Http404 from err

    def get(self, request: RequestInterest, request_id: str) -> Response:
        """
        Get all interests from a specific request
            :param request: Request Interest object
            :param request_id: request's primary key
            :return: all interests from specific request object
        """
        interests = self.get_object(request_id)
        serializer = RequestInterestSerializer(interests, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# pylint: disable=too-many-ancestors
class RequestInterestDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Request Interest details
        :param RetrieveUpdateDestroyAPIView

        * Requires JWT authentication
        * Only authenticated users should be allowed to retrieve, modify or
          delete an interest.
    """

    permission_classes = (IsAuthenticated,)
    lookup_field = "interest_id"
    queryset = RequestInterest.objects.all()
    serializer_class = RequestInterestSerializer
