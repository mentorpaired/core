"""
Language View
"""
from rest_framework import generics

from ..models import LanguageProficiency, SpokenLanguage
from ..serializers import (LanguageProficiencySerializer,
                           SpokenLanguageSerializer)


class LanguageProficiencyList(generics.ListAPIView):
    """ Language proficiencies view """
    queryset = LanguageProficiency.objects.all()
    serializer_class = LanguageProficiencySerializer


class LanguageProficiencyDetail(generics.RetrieveAPIView):
    """ Language proficiency view """
    queryset = LanguageProficiency.objects.all()
    serializer_class = LanguageProficiencySerializer


class LanguageList(generics.ListCreateAPIView):
    """ Spoken languages view """
    queryset = SpokenLanguage.objects.all()
    serializer_class = SpokenLanguageSerializer


class LanguageDetail(generics.RetrieveUpdateDestroyAPIView):
    """ Spoken language view """
    queryset = SpokenLanguage.objects.all()
    serializer_class = SpokenLanguageSerializer
