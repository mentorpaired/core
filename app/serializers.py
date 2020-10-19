"""
Serializers
"""
from rest_framework import serializers

from app.models import (
    LanguageProficiency,
    Pronoun,
    Request,
    RequestInterest,
    Role,
    Skill,
    SkillProficiency,
    SpokenLanguage,
    User,
)


class RoleSerializer(serializers.ModelSerializer):
    """ Role serializer """

    class Meta:
        """ serializer metadata """

        model = Role
        fields = ["role"]


class SkillProficiencySerializer(serializers.ModelSerializer):
    """ SkillProficiency serializer """

    class Meta:
        """ serializer metadata """

        model = SkillProficiency
        fields = ["id", "level"]


class SkillSerializer(serializers.ModelSerializer):
    """ Skill serializer """

    class Meta:
        """ serializer metadata """

        model = Skill
        fields = ["id", "name", "proficiency"]


class LanguageProficiencySerializer(serializers.ModelSerializer):
    """ LanguageProficiency serializer """

    class Meta:
        """ serializer metadata """

        model = LanguageProficiency
        fields = ["id", "level"]


class SpokenLanguageSerializer(serializers.ModelSerializer):
    """ SpokenLanguage serializer """

    class Meta:
        """ serializer metadata """

        model = SpokenLanguage
        fields = ["id", "name", "proficiency"]


class PronounSerializer(serializers.ModelSerializer):
    """ Pronoun serializer """

    class Meta:
        """ serializer metadata """

        model = Pronoun
        fields = ["pronoun"]


class UserSerializer(serializers.ModelSerializer):
    """ User serializer """

    class Meta:
        """ serializer metadata """

        model = User
        fields = [
            "user_id",
            "username",
            "email",
            "role",
            "about",
            "avatar",
            "skills",
            "pronoun",
            "spoken_languages",
            "timezone",
            "availability",
        ]

    def update(self, instance, validated_data):
        """ Update User instance"""
        role = validated_data.get("role")
        if role:
            instance.role.add(*role)

        skills = validated_data.get("skills")
        if skills:
            instance.skills.add(*skills)

        spoken_languages = validated_data.get("spoken_languages")
        if spoken_languages:
            instance.spoken_languages.add(*spoken_languages)

        instance.username = validated_data.get("username", instance.username)
        instance.email = validated_data.get("email", instance.email)
        instance.about = validated_data.get("about", instance.about)
        instance.pronoun = validated_data.get("pronoun", instance.pronoun)
        instance.timezone = validated_data.get("timezone", instance.timezone)
        instance.availability = validated_data.get(
            "availability", instance.availability
        )
        instance.save()
        return instance


class RequestSerializer(serializers.ModelSerializer):
    """ Request serializer """

    class Meta:
        """ serializer metadata """

        model = Request
        fields = ["id", "skill", "description", "mentee", "mentor", "status"]

    def update(self, instance, validated_data):
        instance.skill = validated_data.get("skill", instance.skill)
        instance.description = validated_data.get("description", instance.description)
        instance.mentee = validated_data.get("mentee", instance.mentee)
        instance.status = validated_data.get("status", instance.status)
        instance.mentor = validated_data.get("mentor", instance.mentor)
        instance.description = validated_data.get("description", instance.description)
        instance.save()
        return instance


class RequestInterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestInterest
        fields = [
            "request",
            "mentor",
            "description",
            "status",
        ]

    def update(self, instance, validated_data):
        instance.request = validated_data.get("request", instance.request)
        instance.mentor = validated_data.get("mentor", instance.mentor)
        instance.description = validated_data.get("description", instance.description)
        instance.status = validated_data.get("status", instance.status)
        instance.save()
        return instance
