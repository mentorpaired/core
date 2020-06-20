from rest_framework.test import APIClient, APITestCase

from ..models import (LanguageProficiency, Pronoun, Role, Skill,
                      SkillProficiency, SpokenLanguage, User)


class BaseTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.role = Role.objects.create(
            role="Test"
        )
        self.role2 = Role.objects.create(
            role="Test2"
        )
        self.pronoun = Pronoun.objects.create(
            pronoun="Test"
        )
        self.skillproficiency = SkillProficiency.objects.create(
            level="X"
        )
        self.skill = Skill.objects.create(
            name="Test Programming Language",
            proficiency=self.skillproficiency
        )
        self.skill2 = Skill.objects.create(
            name="Another test programming language",
            proficiency=self.skillproficiency
        )
        self.languageproficiency = LanguageProficiency.objects.create(
            level="X"
        )
        self.spoken_language = SpokenLanguage.objects.create(
            name="Test Spoken Language",
            proficiency=self.languageproficiency
        )
        self.user = User.objects.create(
            display_name="Test User",
            about="Lorem Ipsum text",
            avatar="test.png",
            pronoun=self.pronoun,
            website="www.test.com",
            timezone="Testcontinent/testcountry"
        )
        self.user.role.add(self.role.id)
        self.user.skills.add(self.skill.id)
        self.user.spoken_languages.add(self.spoken_language.id)
        self.user.save()

    def tearDown(self):
        Role.objects.all().delete()
        Pronoun.objects.all().delete()
        Skill.objects.all().delete()
        SpokenLanguage.objects.all().delete()
        User.objects.all().delete()