import graphene
# import django_filters
from graphene_django import DjangoObjectType
# from graphene_django.filter import DjangoFilterConnectionField


from .models import User, Stack, SpokenLanguage, Request, InterestedMentor

# The types below are objects (models) that contain fields, created using relay


class UserNode(DjangoObjectType):
    model = User
    fields = [
        'mentor',
        'mentee',
        'user_id',
        'display_name',
        'about',
        'avatar',
        'stacks',
        'preferred_pronouns',
        'spoken_languages',
        'website',
        'timezone',
        'availability']
    interfaces = (graphene.relay.Node, )


class StackNode(DjangoObjectType):
    model = Stack
    fields = ['name', 'proficiency']
    interfaces = (graphene.relay.Node, )


class SpokenLanguageNode(DjangoObjectType):
    model = SpokenLanguage
    fields = ['name', 'proficiency']
    interfaces = (graphene.relay.Node, )


class RequestNode(DjangoObjectType):
    model = Request
    fields = ['stack', 'description', 'mentee', 'interested_mentors', 'matched_mentor']
    interfaces = (graphene.relay.Node, )


class InterestedMentorNode(DjangoObjectType):
    model = InterestedMentor
    fields = ['name', 'personalised_note', 'accepted']
    interfaces = (graphene.relay.Node, )

# Create Query


class Query(graphene.ObjectType):
    relay_user = graphene.relay.Node.Field(UserNode)
    relay_stack = graphene.relay.Node.Field(StackNode)
    relay_spoken_language = graphene.relay.Node.Field(SpokenLanguageNode)
    relay_request = graphene.relay.Node.Field(RequestNode)
    relay_interested_mentor = graphene.relay.Node.Field(InterestedMentorNode)
