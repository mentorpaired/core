"""
Language View
"""
from rest_framework import viewsets

from ..models import LanguageProficiency, SpokenLanguage
from ..serializers import LanguageProficiencySerializer, SpokenLanguageSerializer


# pylint: disable=too-many-ancestors
class LanguageProficiencyViewSet(viewsets.ModelViewSet):
    """
    Language viewset
        :param: LanguageProficiency object
        :return: Gets all language proficiencies, creates a new proficiency,
        retrieves, updates or deletes an existing proficiency.
    """

    queryset = LanguageProficiency.objects.all()
    serializer_class = LanguageProficiencySerializer


# pylint: disable=too-many-ancestors
class LanguageViewSet(viewsets.ModelViewSet):
    """
    Spoken languages viewset
        :param: Spoken language object
        :return: Get all languages, creates a new language,
        retrieves, updates or deletes an existing language.
    """

    queryset = SpokenLanguage.objects.all()
    serializer_class = SpokenLanguageSerializer
