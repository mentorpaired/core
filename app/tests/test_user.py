from ..models import User
from ..serializers import UserSerializer

from .base import BaseTestCase


class TestUserViews(BaseTestCase):
    def test_get_all_users(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token)
        response = self.client.get("/users")
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)

    def test_get_all_mentors(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token)
        response = self.client.get("/mentors")
        mentors = User.objects.filter(role=self.mentor_role.id)
        serializer = UserSerializer(mentors, many=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)

    def test_retrieve_valid_single_user(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token)
        response = self.client.get(f"/users/{self.profile.pk}")
        user = User.objects.get(pk=self.profile.user_id)
        serializer = UserSerializer(user)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, 200)

    def test_retrieve_invalid_single_user(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token)
        response = self.client.get("/users/10")
        self.assertEqual(response.status_code, 404)

    def test_cannot_create_new_user_without_email_field(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token)
        response = self.client.post(
            "/users",
            {
                "role": [
                    self.mentee_role.id,
                ],
                "username": "testuserx",
                "about": "bio",
                "avatar": "https://dummyavatars.githubcontent.com/u/3",
                "pronoun": self.pronoun.id,
                "skills": [
                    self.beginner_python.id,
                ],
                "spoken_languages": [
                    self.spoken_language.id,
                ],
                "timezone": "Africa/Lagos",
            },
        )
        self.assertEqual(response.status_code, 400)

    def test_create_new_user(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token)
        response = self.client.post(
            "/users",
            {
                "role": [
                    self.mentor_role.id,
                ],
                "username": "testuserone",
                "email": "email@email.com",
                "about": "test bio",
                "avatar": "https://dummyavatars.githubcontent.com/u/2",
                "pronoun": self.pronoun.id,
                "skills": [
                    self.intermediate_python.id,
                ],
                "spoken_languages": [
                    self.spoken_language.id,
                ],
                "timezone": "Africa/Lagos",
            },
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(User.objects.count(), 6)

    def test_update_fields_in_single_user(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token)
        response = self.client.put(
            f"/users/{self.profile.user_id}",
            {
                "role": [self.mentee_role.id],
                "email": "testemail@testemail.com",
                "username": "testusertwo",
                "skills": [self.beginner_python.id],
                "timezone": "Africa/Cairo",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["username"], "testusertwo")
        self.assertEqual(response.data["email"], "testemail@testemail.com")
        self.assertEqual(
            response.data["role"], [self.admin_role.id, self.mentee_role.id]
        )
        self.assertEqual(
            response.data["skills"],
            [self.beginner_python.id, self.intermediate_python.id],
        ),
        self.assertEqual(response.data["timezone"], "Africa/Cairo")

    def test_delete_single_user(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token)
        response = self.client.delete(f"/users/{self.profile.user_id}")
        self.assertEqual(response.status_code, 204)
