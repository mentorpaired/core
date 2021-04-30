import logging

from django.http import Http404

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from ..models import Goal
from ..serializers import GoalSerializer
from ..permissions import IsOwnerOrReadOnly


class GoalViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    queryset = Goal.objects.all()
    serializer_class = GoalSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class RetrieveUserGoal(APIView):
    def get_object(self, pk):
        try:
            return Goal.objects.filter(user=pk)
        except Goal.DoesNotExist:
            logging.warning(f"Goals for user with id {pk} doesn't exist.")
            raise Http404

    def get(self, request, pk):
        goals = self.get_object(pk)
        serializer = GoalSerializer(goals, many=True)
        return Response(serializer.data)
