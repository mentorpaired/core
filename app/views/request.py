from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Request
from ..serializers import RequestSerializer


class RequestList(APIView):

    def get(self, request):
        requests = Request.objects.all()
        serializer = RequestSerializer(requests, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RequestSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RequestDetail(APIView):

    """ def get_object(self, pk):
        try:
            return Request.objects.get(id=pk)
        except Request.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        requests = self.get_object(pk)
        serializer = RequestSerializer(requests)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        requests = self.get_object(pk)
        serializer = RequestSerializer(requests, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        requests = self.get_object(pk)
        serializer = RequestSerializer(requests, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        requests = self.get_object(pk)
        requests.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)"""


class RequestInterestList(APIView):
    """def get(self, request):
        request_interests = RequestInterest.objects.all()
        serializer = RequestInterestSerializer(interests, many=True)
        return Response(serializer.data)

    def get_object(self, pk):
        try:
            return Request.objects.get(id=pk)
        except Request.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        requests = self.get_object(pk)
        serializer = RequestSerializer(requests)
        return Response(serializer.data)"""
