from ..models import (
    Pronoun,
    Request,
    RequestInterest,
    Role,
    Skill,
    Goal,
    SpokenLanguage,
    User,
)
from .base import BaseTestCase


class TestCreateModels(BaseTestCase):
    def test_role_is_created(self):
        self.assertEqual(Role.objects.count(), 3)
        self.assertEqual(self.admin_role.role, "ADMIN")

    def test_skills_is_created(self):
        self.assertEqual(Skill.objects.count(), 2)
        self.assertEqual(self.beginner_python.name, "Python Beginner")

    def test_language_is_created(self):
        self.assertEqual(SpokenLanguage.objects.count(), 1)
        self.assertEqual(self.spoken_language.name, "English")

    def test_pronoun_is_created(self):
        self.assertEqual(Pronoun.objects.count(), 1)
        self.assertEqual(self.pronoun.pronoun, "She/Her")

    def test_user_is_created(self):
        self.assertEqual(User.objects.count(), 5)
        self.assertTrue(hasattr(self.profile, "skills"), True)
        self.assertTrue(self.profile.skills, self.beginner_python.id)

    def test_request_is_created(self):
        self.assertEqual(Request.objects.count(), 1)
        self.assertTrue(hasattr(self.request, "mentee"), True)
        self.assertTrue(self.request.skill, self.intermediate_python)

    def test_request_interest_is_created(self):
        self.assertEqual(RequestInterest.objects.count(), 1)
        self.assertTrue(hasattr(self.request_interest, "mentor"), True)
        self.assertTrue(self.request_interest.status, "OPEN")

    def test_goal_is_created(self):
        self.assertEqual(Goal.objects.count(), 1)
        self.assertTrue(hasattr(self.goal, "goal"), True)
        self.assertTrue(self.goal.goal, "Learn TypeScript")
