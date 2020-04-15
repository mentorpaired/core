from app.models import Stack, SpokenLanguage, User, InterestedMentor, Request
from rest_framework import serializers


class StackSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Stack
        fields = ['name', 'proficiency']
    

class SpokenLanguageSerializer(serializers.ModelSerializer):

    class Meta:
        model = SpokenLanguage
        fields = ['name', 'proficiency']


class UserSerializer(serializers.ModelSerializer):
    stacks = StackSerializer(many=True)
    spoken_languages = SpokenLanguageSerializer(many=True)

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
    
    def create(self, validated_data):
        stacks_data = validated_data.pop('stacks')
        languages_data = validated_data.pop('spoken_languages')
        user = User.objects.create(**validated_data)
        for stack_data in stacks_data:
            Stack.objects.create(user=user, **stack_data)
        for language_data in languages_data:
            SpokenLanguage.objects.create(user=user, **language_data)
        return user


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
