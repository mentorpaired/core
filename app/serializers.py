from app.models import Stack, SpokenLanguage, User, InterestedMentor, Request
from rest_framework import serializers


class StackSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stack
        fields = ['name', 'proficiency']


class SpokenLanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SpokenLanguage
        fields = ['name', 'proficiency']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            'user_id',
            'mentor',
            'mentee',
            'display_name',
            'about',
            'avatar',
            'stacks',
            'pronouns',
            'spoken_languages',
            'timezone',
            'availability'
        ]


class InterestedMentorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InterestedMentor
        fields = [
            'name',
            'personalised_note',
            'accepted'
        ]


class RequestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Request
        fields = [
            'stack',
            'description',
            'mentee',
            'interested_mentors',
            'matched_mentor'
        ]
