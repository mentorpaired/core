from rest_framework.test import APIClient, APITestCase

from ..models import (LanguageProficiency, Pronoun, Request, Role, Skill,
                      SkillProficiency, SpokenLanguage, User)


class BaseTestCase(APITestCase):

    def setUp(self):

        self.client = APIClient()

        self.admin = User.objects.create_superuser(
            username='test',
            email='test@test.com',
            password='testpassword'
        )

        self.assertEqual(self.admin.is_active, 1, 'Active User')

        self.admin_login = self.client.post('/api/token/', {
            'username': 'test',
            'password': 'testpassword',
        }, format='json')

        self.assertEqual(self.admin_login.status_code, 200)

        self.token = self.admin_login.data['access']

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
            username="testuser",
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

        self.request_mentee = User.objects.create(
            username="Second user",
            about="Random bio of second user",
            avatar="https://dummyavatars.githubcontent.com/u/0",
            pronoun=self.pronoun,
            website="www.secondtestsite.com",
            timezone="Secondcontinent/secondcountry"
        )
        self.request_mentee.role.add(self.role2.id)
        self.request_mentee.skills.add(self.skill2.id)
        self.request_mentee.spoken_languages.add(self.spoken_language.id)
        self.request_mentee.save()

        self.request = Request.objects.create(
            skill=self.skill2,
            description="Short text about a request for mentorship",
            mentee=self.request_mentee,
            status="OPEN"
        )

    def tearDown(self):
        Role.objects.all().delete()
        Pronoun.objects.all().delete()
        Skill.objects.all().delete()
        SpokenLanguage.objects.all().delete()
        User.objects.all().delete()
