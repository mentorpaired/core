from .base import BaseTestCase


class TestAuthenticationCase(BaseTestCase):
    def test_successful_login_and_token_generation(self):
        response = self.client.post(
            "/api/token/", {"username": "test", "password": "testpassword"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("access", response.data)

        def test_valid_user_can_refresh_access_token(self):
            response = self.client.get(
                "/api/token/refresh/", {"refresh": self.response.data["refresh"]}
            )
            self.assertEqual(response.status_code, 200)

    def test_nonexistent_superuser_cannot_create_new_token(self):
        response = self.client.post(
            "/api/token/", {"username": "random", "password": "testing"}
        )
        self.assertEqual(response.status_code, 401)
