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
    all_relay_spoken_language = DjangoFilterConnectionField(
        SpokenLanguageNode, filterset_class=SpokenLanguageFilter)

    relay_request = graphene.relay.Node.Field(RequestNode)
    all_relay_request = DjangoFilterConnectionField(RequestNode, filterset_class=RequestFilter)

    relay_interested_mentor = graphene.relay.Node.Field(InterestedMentorNode)
    all_relay_interested_mentor = DjangoFilterConnectionField(
        InterestedMentorNode, filterset_class=InterestedMentorFilter)


# Mutation - for sending data to the server
class CreateUser(graphene.relay.ClientIDMutation):
    user = graphene.Field(UserNode)

    class Input:
        mentor = graphene.Boolean(default=False)
        mentee = graphene.Boolean(default=True)
        # user_id = graphene.UUID()
        display_name = graphene.String(required=True)
        about = graphene.String()
        stacks = graphene.String()
        preferred_pronouns = graphene.String()
        spoken_languages = graphene.String()
        timezone = graphene.Date()
        availability = graphene.Boolean(default=False)

    stack = graphene.Field(StackNode)
    spoken_languages = graphene.Field(SpokenLanguageNode)

    def mutate_and_get_payload(root, info, **input):
        user = User(
            mentor=input.get('mentor'),
            mentee=input.get('mentee'),
            # user_id=input.get('user_id'),
            display_name=input.get('display_name'),
            about=input.get('about'),
            stacks=create_stack('name', 'proficiency'),
            preferred_pronouns=input.get('preferred_pronouns'),
            spoken_languages=create_language('name', 'proficiency'),
            timezone=input.get('timezone'),
            availability=input.get('availability'),
            )
        user.save()

        return CreateUser(user=user)

'''Commenting out stack and spoken_languages because I do not think I need to create them as their own entities, going by the relationship in models.py'''

# class CreateStack(graphene.relay.ClientIDMutation):
#     stack = graphene.Field(StackNode)

#     class Input:
#         name = graphene.String()
#         proficiency = graphene.String()

#     def mutate_and_get_payload(root, info, **input):
#         stack = Stack(
#             name=input.get('name'),
#             proficiency=input.get('proficiency'),
#         )
#         stack.save()

#         return CreateStack(stack=stack)


# class CreateSpokenLanguage(graphene.relay.ClientIDMutation):
#     spoken_language = graphene.Field(SpokenLanguageNode)

#     class Input:
#         name = graphene.String()
#         proficiency = graphene.String()

#     def mutate_and_get_payload(root, info, **input):
#         spoken_language = SpokenLanguage(
#             name=input.get('name'),
#             proficiency=input.get('proficiency'),
#         )
#         spoken_language.save()

#         return CreateSpokenLanguage(spoken_language=spoken_language)


class CreateRequest(graphene.relay.ClientIDMutation):
    request = graphene.Field(RequestNode)

    class Input:
        stack = graphene.String(description='Stack you\'d like to learn')
        description = graphene.String(description='Additional information you think will be helpful for you, your available dates, etc.')
        mentee = graphene.String()
        interested_mentors = graphene.String()
        matched_mentor = graphene.String()

    stack = graphene.Field(StackNode)
    mentee = graphene.Field(UserNode)
    interested_mentors = graphene.Field(UserNode)
    matched_mentor = graphene.Field(UserNode)

    def mutate_and_get_payload(root, info, **input):
        request = Request(
            stack=create_stack('name', 'proficiency'),
            description=input.get('description'),
            mentee=create_user('mentee'),
            interested_mentors=input.get('interested_mentors'),
            matched_mentor=input.get('matched_mentor'),
        )
        request.save()

        return CreateRequest(request=request)


class CreateInterestedMentor(graphene.relay.ClientIDMutation):
    interested_mentor = graphene.Field(InterestedMentorNode)

    class Input:
        name = graphene.String()
        personalised_note = graphene.String()
        accepted = graphene.Boolean(default=False)

    name = graphene.Field(UserNode)

    def mutate_and_get_payload(root, info, **input):
        interested_mentor = InterestedMentor(
            name=input.get('name'),
            personalised_note=input.get('personalised_note'),
            accepted=input.get('accepted'),
        )
        interested_mentor.save()

        return CreateInterestedMentor(interested_mentor=interested_mentor)


class Mutation(graphene.AbstractType):
    create_user = CreateUser.Field()
    # create_stack = CreateStack.Field()
    # create_spoken_language = CreateSpokenLanguage.Field()
    create_request = CreateRequest.Field()
    create_interested_mentor = CreateInterestedMentor.Field()
