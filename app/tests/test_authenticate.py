from django.contrib.auth.models import User

from .base import BaseTestCase


class AuthenticationTestCase(BaseTestCase):

    def test_successful_superuser_creation(self):
        self.second_superuser = User.objects.create_superuser(
            username='testusertwo',
            email='testusertwo@test.com',
            password='testusertwopassword'
        )
        self.assertEqual(User.objects.count(), 2)

        def test_successful_login_and_token_generation(self):
            response = self.client.post('/api/token/', {
                'username': 'testusertwo',
                'password': 'testusertwopassword'
            })
            self.assertEqual(response.status_code, 200)
            self.assertIn('access', self.response.data)

        def test_valid_user_can_refresh_access_token(self):
            response = self.client.get('/api/token/refresh/', {
                'refresh': response.data['refresh']
            })
            self.assertEqual(response.status_code, 200)


    def test_noexistent_superuser_cannot_create_new_token(self):
        response = self.client.post('/api/token/', {
            'username': 'random',
            'password': 'testing'
        })
        self.assertEqual(response.status_code, 401)