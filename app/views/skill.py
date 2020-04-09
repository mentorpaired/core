from rest_framework import generics

from ..models import Skill, SkillProficiency
from ..serializers import SkillSerializer, SkillProficiencySerializer


class SkillProficiencyList(generics.ListAPIView):

    queryset = SkillProficiency.objects.all()
    serializer_class = SkillProficiencySerializer


class SkillProficiencyDetail(generics.RetrieveAPIView):

    queryset = SkillProficiency.objects.all()
    serializer_class = SkillProficiencySerializer


class SkillList(generics.ListCreateAPIView):

    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class SkillDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
