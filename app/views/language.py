"""
Language View
"""
from rest_framework import viewsets

from ..models import LanguageProficiency, SpokenLanguage
from ..serializers import LanguageProficiencySerializer, SpokenLanguageSerializer


# pylint: disable=too-many-ancestors
class LanguageProficiencyViewSet(viewsets.ModelViewSet):
    """ Language viewset """

    queryset = LanguageProficiency.objects.all()
    serializer_class = LanguageProficiencySerializer


# pylint: disable=too-many-ancestors
class LanguageViewSet(viewsets.ModelViewSet):
    """ Spoken languages viewset """

    queryset = SpokenLanguage.objects.all()
    serializer_class = SpokenLanguageSerializer
