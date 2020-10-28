"""
Skill view
"""
from rest_framework import viewsets

from ..models import Skill, SkillProficiency
from ..serializers import SkillProficiencySerializer, SkillSerializer


# pylint: disable=too-many-ancestors
class SkillProficiencyViewSet(viewsets.ModelViewSet):
    """
    Skill proficiencies viewset
        :param: SkillProficiency object
        :return: Gets all skill proficiencies, creates a new proficiency,
        retrieves, updates or deletes an existing proficiency.
    """

    queryset = SkillProficiency.objects.all()
    serializer_class = SkillProficiencySerializer


# pylint: disable=too-many-ancestors
class SkillViewSet(viewsets.ModelViewSet):
    """
    Skills viewset
        :param: Skill object
        :return: Get all skills, create a new skill,
        retrieves, updates or deletes an existing skill.
    """

    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
