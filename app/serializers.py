from rest_framework import serializers

from app.models import (
    Skill, SpokenLanguage, User, Role, Pronoun,
    LanguageProficiency, SkillProficiency
)


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