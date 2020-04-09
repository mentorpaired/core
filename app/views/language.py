from rest_framework import generics

from ..models import LanguageProficiency, SpokenLanguage
from ..serializers import LanguageProficiencySerializer, SpokenLanguageSerializer


class LanguageProficiencyList(generics.ListAPIView):

    queryset = LanguageProficiency.objects.all()
    serializer_class = LanguageProficiencySerializer


class LanguageProficiencyDetail(generics.RetrieveAPIView):

    queryset = LanguageProficiency.objects.all()
    serializer_class = LanguageProficiencySerializer


class LanguageList(generics.ListCreateAPIView):

    queryset = SpokenLanguage.objects.all()
    serializer_class = SpokenLanguageSerializer


class LanguageDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = SpokenLanguage.objects.all()
    serializer_class = SpokenLanguageSerializer
