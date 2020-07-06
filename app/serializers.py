from rest_framework import serializers

from app.models import (LanguageProficiency, Pronoun, Role, Skill,
                        SkillProficiency, SpokenLanguage, User, Request)
from app.models import (GithubAuth, LanguageProficiency, Pronoun, Role, Skill,
                        SkillProficiency, SpokenLanguage, User)


class RoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Role
        fields = ['role']


class SkillProficiencySerializer(serializers.ModelSerializer):

    class Meta:
        model = SkillProficiency
        fields = ['id', 'level']


class SkillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skill
        fields = ['id', 'name', 'proficiency']


class LanguageProficiencySerializer(serializers.ModelSerializer):

    class Meta:
        model = LanguageProficiency
        fields = ['id', 'level']


class SpokenLanguageSerializer(serializers.ModelSerializer):

    class Meta:
        model = SpokenLanguage
        fields = ['id', 'name', 'proficiency']


class PronounSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pronoun
        fields = ['pronoun']


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'user_id',
            'role',
            'display_name',
            'about',
            'avatar',
            'skills',
            'pronoun',
            'spoken_languages',
            'timezone',
            'availability'
        ]

    def update(self, instance, validated_data):

        role = validated_data.get('role')
        if role:
            instance.role.add(*role)

        skills = validated_data.get('skills')
        if skills:
            instance.skills.add(*skills)

        spoken_languages = validated_data.get('spoken_languages')
        if spoken_languages:
            instance.spoken_languages.add(*spoken_languages)

        instance.display_name = validated_data.get('display_name', instance.display_name)
        instance.about = validated_data.get('about', instance.about)
        instance.pronoun = validated_data.get('pronoun', instance.pronoun)
        instance.timezone = validated_data.get('timezone', instance.timezone)
        instance.availability = validated_data.get('availability', instance.availability)
        instance.save()
        return instance


class RequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Request
        fields = [
            'id',
            'skill',
            'description',
            'mentee',
            'mentor',
            'status'
        ]

    def update(self, instance, validated_data):
        instance.skill = validated_data.get('skill', instance.skill)
        instance.description = validated_data.get('description', instance.description)
        instance.mentor = validated_data.get('mentor', instance.mentor)
        instance.status = validated_data.get('status', instance.status)
        instance.mentor = validated_data.get('mentor', instance.mentor)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance


class GithubAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = GithubAuth
        fields = ['github_user_id', 'oauth_token', 'domain_name', 'user_profile']
