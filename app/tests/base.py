import logging
from rest_framework.test import APIClient, APITestCase

from ..models import (
    LanguageProficiency,
    Pronoun,
    Request,
    RequestInterest,
    Role,
    Skill,
    Goal,
    SkillProficiency,
    SpokenLanguage,
    User,
)


class BaseTestCase(APITestCase):
    def setUp(self):
        logging.disable(logging.CRITICAL)

        self.client = APIClient()

        self.admin = User.objects.create_superuser(
            username="test", email="test@test.com", password="testpassword"
        )
        self.second_admin = User.objects.create_superuser(
            username="second admin", email="test2@test2.com", password="test2password"
        )

        self.assertEqual(self.admin.is_active, 1, "Active User")

        self.admin_login = self.client.post(
            "/api/token/",
            {
                "username": "test",
                "password": "testpassword",
            },
            format="json",
        )

        self.second_admin_login = self.client.post(
            "/api/token/", {"username": "second admin", "password": "test2password"}
        )

        self.assertEqual(self.admin_login.status_code, 200)
        self.assertEqual(self.second_admin_login.status_code, 200)

        self.token = self.admin_login.data["access"]
        self.second_token = self.second_admin_login.data["access"]

        self.admin_role = Role.objects.create(role="ADMIN")
        self.mentor_role = Role.objects.create(role="MENTOR")
        self.mentee_role = Role.objects.create(role="MENTEE")
        self.pronoun = Pronoun.objects.create(pronoun="She/Her")
        self.beginner_skill_proficiency = SkillProficiency.objects.create(level="B")
        self.intermediate_skill_proficiency = SkillProficiency.objects.create(level="I")
        self.beginner_python = Skill.objects.create(
            name="Python Beginner",
            proficiency=self.beginner_skill_proficiency,
        )
        self.intermediate_python = Skill.objects.create(
            name="Intermediate Python",
            proficiency=self.intermediate_skill_proficiency,
        )
        self.native_language_proficiency = LanguageProficiency.objects.create(
            level="NBP"
        )
        self.spoken_language = SpokenLanguage.objects.create(
            name="English", proficiency=self.native_language_proficiency
        )
        self.profile = User.objects.create(
            username="testuser",
            email="testemail@testemail.com",
            about="Lorem Ipsum text",
            avatar="https://dummyavatars.githubcontent.com/u/1",
            pronoun=self.pronoun,
            website="www.test.com",
            timezone="Testcontinent/testcountry",
        )
        self.profile.role.add(self.admin_role.id)
        self.profile.skills.add(self.intermediate_python.id)
        self.profile.spoken_languages.add(self.spoken_language.id)
        self.profile.save()

        self.request_mentee = User.objects.create(
            username="Second user",
            email="requestmentee@email.com",
            about="Random bio of second user",
            avatar="https://dummyavatars.githubcontent.com/u/0",
            pronoun=self.pronoun,
            website="www.secondtestsite.com",
            timezone="Secondcontinent/secondcountry",
        )
        self.request_mentee.role.add(self.mentee_role.id)
        self.request_mentee.skills.add(self.beginner_python.id)
        self.request_mentee.spoken_languages.add(self.spoken_language.id)
        self.request_mentee.save()

        self.request = Request.objects.create(
            skill=self.intermediate_python,
            description="Short text about a request for mentorship",
            mentee=self.request_mentee,
            status="OPEN",
        )

        self.request_mentor = User.objects.create(
            username="Third user",
            email="requestmentor@email.com",
            about="Random bio of third user",
            avatar="https://dummyavatars.githubcontent.com/u/0",
            pronoun=self.pronoun,
            website="www.thirdtestsite.com",
            timezone="Thirdcontinent/thirdcountry",
        )
        self.request_mentor.role.add(self.mentor_role.id)
        self.request_mentor.role.add(self.admin_role.id)
        self.request_mentor.skills.add(self.intermediate_python.id)
        self.request_mentor.spoken_languages.add(self.spoken_language.id)
        self.request_mentor.save()

        self.request_interest = RequestInterest.objects.create(
            request=self.request,
            mentor=self.profile,
            description="Short description about mentor's interest",
            status="OPEN",
        )

        self.goal = Goal.objects.create(
            user=self.admin,
            goal="Learn TypeScript",
            description="Need a mentor, I'm trying to learn the advanced topics of TypeScript.",
        )

    def tearDown(self):
        Role.objects.all().delete()
        Pronoun.objects.all().delete()
        Skill.objects.all().delete()
        SpokenLanguage.objects.all().delete()
        User.objects.all().delete()
        Request.objects.all().delete()
        RequestInterest.objects.all().delete()

        logging.disable(logging.NOTSET)
