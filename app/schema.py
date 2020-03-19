import graphene
import django_filters
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField


from .models import User, Stack, SpokenLanguage, Request, InterestedMentor

# The types below are objects (models) that contain fields, created using relay


class UserFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = [
            'mentor',
            'mentee',
            'user_id',
            'display_name',
            'about',
            # 'avatar',
            'stacks',
            'preferred_pronouns',
            'spoken_languages',
            'website',
            'timezone',
            'availability']


class UserNode(DjangoObjectType):
    class Meta:
        model = User
        interfaces = (graphene.relay.Node, )


class StackFilter(django_filters.FilterSet):
    class Meta:
        model = Stack
        fields = ['name', 'proficiency']


class StackNode(DjangoObjectType):
    class Meta:
        model = Stack
        interfaces = (graphene.relay.Node, )


class SpokenLanguageFilter(django_filters.FilterSet):
    class Meta:
        model = SpokenLanguage
        fields = ['name', 'proficiency']


class SpokenLanguageNode(DjangoObjectType):
    class Meta:
        model = SpokenLanguage
        interfaces = (graphene.relay.Node, )


class RequestFilter(django_filters.FilterSet):
    class Meta:
        model = Request
        fields = ['stack', 'description', 'mentee', 'interested_mentors', 'matched_mentor']


class RequestNode(DjangoObjectType):
    class Meta:
        model = Request
        interfaces = (graphene.relay.Node, )


class InterestedMentorFilter(django_filters.FilterSet):
    class Meta:
        model = InterestedMentor
        fields = ['name', 'personalised_note', 'accepted']

class InterestedMentorNode(DjangoObjectType):
    class Meta:
        model = InterestedMentor
        interfaces = (graphene.relay.Node, )

# Create Query


class Query(graphene.ObjectType):
    relay_user = graphene.relay.Node.Field(UserNode)
    all_relay_user = DjangoFilterConnectionField(UserNode, filterset_class=UserFilter)

    relay_stack = graphene.relay.Node.Field(StackNode)
    all_relay_stack = DjangoFilterConnectionField(StackNode, filterset_class=StackFilter)

    relay_spoken_language = graphene.relay.Node.Field(SpokenLanguageNode)
    all_relay_spoken_language = DjangoFilterConnectionField(SpokenLanguageNode, filterset_class=SpokenLanguageFilter)

    relay_request = graphene.relay.Node.Field(RequestNode)
    all_relay_request = DjangoFilterConnectionField(RequestNode, filterset_class=RequestFilter)

    relay_interested_mentor = graphene.relay.Node.Field(InterestedMentorNode)
    all_relay_interested_mentor = DjangoFilterConnectionField(InterestedMentorNode, filterset_class=InterestedMentorFilter)
