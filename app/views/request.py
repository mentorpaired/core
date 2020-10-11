from django.http import Http404
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

    def get_object(self, pk):
        try:
            return Request.objects.get(id=pk)
        except Request.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        request = self.get_object(pk)
        serializer = RequestSerializer(request)
        return Response(serializer.data)

    def put(self, request, pk):
        request_obj = self.get_object(pk)
        serializer = RequestSerializer(request_obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        request = self.get_object(pk)
        request.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
