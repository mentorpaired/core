from ..models import Pronoun, Role, Skill, SpokenLanguage, User

from .base import BaseTestCase


class TestCreateModels(BaseTestCase):

    def test_role_is_created(self):
        self.assertEqual(Role.objects.count(), 2)
        self.assertEqual(self.role2.role, "Test2")

    def test_skills_is_created(self):
        self.assertEqual(Skill.objects.count(), 2)
        self.assertEqual(self.skill.name, "Test Programming Language")

    def test_language_is_created(self):
        self.assertEqual(SpokenLanguage.objects.count(), 1)
        self.assertEqual(self.spoken_language.name, "Test Spoken Language")

    def test_pronoun_is_created(self):
        self.assertEqual(Pronoun.objects.count(), 1)
        self.assertEqual(self.pronoun.pronoun, "Test")

    def test_user_is_created(self):
        self.assertEqual(User.objects.count(), 1)
        self.assertTrue(hasattr(self.user, 'skills'), True)
        self.assertTrue(self.user.skills, self.skill.id)
