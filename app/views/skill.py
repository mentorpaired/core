"""
Skill view
"""
from rest_framework import viewsets

from ..models import Skill, SkillProficiency
from ..serializers import SkillProficiencySerializer, SkillSerializer


# pylint: disable=too-many-ancestors
class SkillProficiencyViewSet(viewsets.ModelViewSet):
    """ Skill proficiencies viewset """

    queryset = SkillProficiency.objects.all()
    serializer_class = SkillProficiencySerializer


# pylint: disable=too-many-ancestors
class SkillViewSet(viewsets.ModelViewSet):
    """ Skills viewset """

    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
