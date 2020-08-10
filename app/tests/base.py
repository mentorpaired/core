from django.contrib.auth.models import User as DefaultUser
from rest_framework.test import APIClient, APITestCase

from ..models import (LanguageProficiency, Pronoun, Role, Skill,
                      SkillProficiency, SpokenLanguage, User)


class BaseTestCase(APITestCase):

    def setUp(self):

        self.client = APIClient()

        self.user = DefaultUser.objects.create_superuser(
            username='test',
            email='test@test.com',
            password='testpassword'
        )

        self.assertEqual(self.user.is_active, 1, 'Active User')

        self.user_login = self.client.post('/api/token/', {
            'username': 'test',
            'password': 'testpassword',
        }, format='json')

        self.assertEqual(self.user_login.status_code, 200)

        self.token = self.user_login.data['access']

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
        self.profile = User.objects.create(
            display_name="Test User",
            about="Lorem Ipsum text",
            avatar="https://dummyavatars.githubcontent.com/u/1",
            pronoun=self.pronoun,
            website="www.test.com",
            timezone="Testcontinent/testcountry"
        )
        self.profile.role.add(self.role.id)
        self.profile.skills.add(self.skill.id)
        self.profile.spoken_languages.add(self.spoken_language.id)
        self.profile.save()

    def tearDown(self):
        Role.objects.all().delete()
        Pronoun.objects.all().delete()
        Skill.objects.all().delete()
        SpokenLanguage.objects.all().delete()
        User.objects.all().delete()
