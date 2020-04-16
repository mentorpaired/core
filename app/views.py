from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.viewsets import GenericViewSet

from .models import Stack, SpokenLanguage, User
from .serializers import StackSerializer, SpokenLanguageSerializer, UserSerializer


class StackViewSet(GenericViewSet, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, ListModelMixin, DestroyModelMixin):

    serializer_class = StackSerializer
    queryset = Stack.objects.all()


class SpokenLanguageViewSet(GenericViewSet, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, ListModelMixin, DestroyModelMixin):

    serializer_class = SpokenLanguageSerializer
    queryset = SpokenLanguage.objects.all()


class UserViewSet(GenericViewSet, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, ListModelMixin, DestroyModelMixin):

    serializer_class = UserSerializer
    queryset = User.objects.all()
