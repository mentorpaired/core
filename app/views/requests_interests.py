from django.http import Http404
import logging

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import RequestInterest
from ..serializers import RequestInterestSerializer


class RequestInterestList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        interests = RequestInterest.objects.all()
        serializer = RequestInterestSerializer(interests, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RequestInterestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MentorRequestInterest(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, id_):
        try:
            return RequestInterest.objects.filter(request_id__exact=id_)
        except RequestInterest.DoesNotExist:
            raise Http404
            logging.warning("Interest for this request object doesn't exist.")

    def get(self, request, id_):
        interests = self.get_object(id_)
        serializer = RequestInterestSerializer(interests, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RequestInterestDetail(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, id_):
        try:
            return RequestInterest.objects.get(id=id_)
        except RequestInterest.DoesNotExist:
            raise Http404
            logging.warning("Interest object doesn't exist.")

    def get(self, request, id_):
        interest = self.get_object(id_)
        serializer = RequestInterestSerializer(interest)
        return Response(serializer.data)

    def put(self, request, id_):
        interest = self.get_object(id_)
        serializer = RequestInterestSerializer(
            interest, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id_):
        interest = self.get_object(id_)
        interest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
