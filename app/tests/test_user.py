from ..models import User
from ..serializers import UserSerializer

from .base import BaseTestCase


class TestUserViews(BaseTestCase):

    def test_get_all_users(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        response = self.client.get('/users/')
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)

    def test_retrieve_valid_single_user(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        response = self.client.get(f'/users/{self.profile.pk}/')
        user = User.objects.get(pk=self.profile.user_id)
        serializer = UserSerializer(user)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, 200)

    def test_retrieve_invalid_single_user(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        response = self.client.get('/users/10/')
        self.assertEqual(response.status_code, 404)

    def test_create_new_user(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        response = self.client.post('/users/', {
            'role': [self.role.id, ],
            'display_name': 'test user',
            'about': 'test bio',
            'avatar': 'https://dummyavatars.githubcontent.com/u/2',
            'pronoun': self.pronoun.id,
            'skills': [self.skill.id, ],
            'spoken_languages': [self.spoken_language.id, ],
            'timezone': 'Africa/Lagos'
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(User.objects.count(), 3)

    def test_update_fields_in_single_user(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        response = self.client.put(f'/users/{self.profile.user_id}/', {
            'role': [self.role2.id],
            'display_name': 'test user2',
            'skills': [self.skill2.id],
            'timezone': 'Africa/Cairo'
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['display_name'], 'test user2')
        self.assertEqual(response.data['role'], [self.role.id, self.role2.id])
        self.assertEqual(response.data['skills'], [self.skill.id, self.skill2.id]),
        self.assertEqual(response.data['timezone'], 'Africa/Cairo')

    def test_delete_single_user(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        response = self.client.delete(f'/users/{self.profile.user_id}/')
        self.assertEqual(response.status_code, 204)
