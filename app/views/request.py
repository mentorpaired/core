from django.http import Http404
import logging

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from ..models import Request
from ..serializers import RequestSerializer


class RequestList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        request = Request.objects.all()
        serializer = RequestSerializer(request, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RequestSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RequestDetail(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, id_):
        try:
            return Request.objects.get(id=id_)
        except Request.DoesNotExist:
            logging.warning("Request object doesn't exist.")
            raise Http404

    def get(self, request, id_):
        request = self.get_object(id_)
        serializer = RequestSerializer(request)
        return Response(serializer.data)

    def put(self, request, id_):
        request_obj = self.get_object(id_)
        serializer = RequestSerializer(request_obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id_):
        request = self.get_object(id_)
        request.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
