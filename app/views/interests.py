from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import RequestInterest
from ..serializers import RequestInterestSerializer


class InterestList(APIView):

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


class RequestInterestList(APIView):

    def get_object(self, pk):
        try:
            return RequestInterest.objects.filter(request_id__exact=pk)
        except RequestInterest.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        interest = self.get_object(pk)
        serializer = RequestInterestSerializer(interest, many=True)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        interest = self.get_object(pk)
        serializer = RequestInterestSerializer(interest, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        interest = self.get_object(pk)
        serializer = RequestInterestSerializer(interest, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        interest = self.get_object(pk)
        interest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
