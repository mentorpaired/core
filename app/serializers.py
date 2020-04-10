from app.models import Stack, SpokenLanguage, User, InterestedMentor, Request
from rest_framework import serializers


class StackSerializer(serializers.PrimaryKeyRelatedField, serializers.ModelSerializer):
    class Meta:
        model = Stack
        fields = ['name', 'proficiency']


class SpokenLanguageSerializer(serializers.PrimaryKeyRelatedField, serializers.ModelSerializer):
    class Meta:
        model = SpokenLanguage
        fields = ['name', 'proficiency']


class UserSerializer(serializers.ModelSerializer):
    stacks = StackSerializer(many=True, queryset=Stack.objects.all())
    spoken_languages = SpokenLanguageSerializer(many=True, queryset=SpokenLanguage.objects.all())

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


class InterestedMentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterestedMentor
        fields = [
            'name',
            'personalised_note',
            'accepted'
        ]


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = [
            'stack',
            'description',
            'mentee',
            'interested_mentors',
            'matched_mentor'
        ]
