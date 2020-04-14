from rest_framework import viewsets
from .models import Stack, SpokenLanguage, User, InterestedMentor, Request
from .serializers import StackSerializer, SpokenLanguageSerializer, UserSerializer, InterestedMentorSerializer, RequestSerializer


class StackViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing stacks.
    """
    queryset = Stack.objects.all()
    serializer_class = StackSerializer


class SpokenLanguageViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing the language(s) a user speaks.
    """
    queryset = SpokenLanguage.objects.all()
    serializer_class = SpokenLanguageSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing the users.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class InterestedMentorViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing the interested mentors.
    """
    queryset = InterestedMentor.objects.all()
    serializer_class = InterestedMentorSerializer


class RequestViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing mentee's requests.
    """
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
