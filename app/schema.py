import graphene
from graphene_django import DjangoObjectType

from .models import User, Stack, SpokenLanguage, Request, InterestedMentor

# The types below are objects (models) that contain fields 
class UserType(DjangoObjectType):
    class Meta:
        model = User

class StackType(DjangoObjectType):
    class Meta:
        model = Stack

class SpokenLanguageType(DjangoObjectType):
    class Meta:
        model = SpokenLanguage

class RequestType(DjangoObjectType):
    class Meta:
        model = Request

class InterestedMentorType(DjangoObjectType):
    class Meta:
        model = InterestedMentor

class Query(graphene.ObjectType):
    users = graphene.List(UserType)
    stacks = graphene.List(StackType)
    spoken_languages = graphene.List(SpokenLanguageType)
    requests = graphene.List(RequestType)
    interested_mentors = graphene.List(InterestedMentorType)

    def resolve_users(self, info, **kwargs):
        return User.objects.all()

    def resolve_stacks(self, info, **kwargs):
        return Stack.objects.all()

    def resolve_spoken_languages(self, info, **kwargs):
        return SpokenLanguage.objects.all()

    def resolve_requests(self, info, **kwargs):
        return Request.objects.all()

    def resolve_interested_mentors(self, info, **kwargs):
        return InterestedMentor.objects.all()
