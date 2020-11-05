from django.http import Http404
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import RequestInterest
from ..serializers import RequestInterestSerializer


class RequestInterestList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        interests = RequestInterest.objects.all()
        serializer = RequestInterestSerializer(interests, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RequestInterestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MentorRequestInterest(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, request_id):
        try:
            return RequestInterest.objects.filter(request_id__exact=request_id)
        except RequestInterest.DoesNotExist:
            raise Http404

    def get(self, request, request_id):
        interests = self.get_object(request_id)
        serializer = RequestInterestSerializer(interests, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RequestInterestDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    lookup_field = "interest_id"
    queryset = RequestInterest.objects.all()
    serializer_class = RequestInterestSerializer
