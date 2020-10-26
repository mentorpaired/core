"""
Skill view
"""
from rest_framework import generics

from ..models import Skill, SkillProficiency
from ..serializers import SkillProficiencySerializer, SkillSerializer


class SkillProficiencyList(generics.ListAPIView):
    """ Skill proficiencies view """

    queryset = SkillProficiency.objects.all()
    serializer_class = SkillProficiencySerializer


class SkillProficiencyDetail(generics.RetrieveAPIView):
    """ Skill proficiency view """

    queryset = SkillProficiency.objects.all()
    serializer_class = SkillProficiencySerializer


class SkillList(generics.ListCreateAPIView):
    """ Skills view """

    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class SkillDetail(generics.RetrieveUpdateDestroyAPIView):
    """ Skill view """

    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
