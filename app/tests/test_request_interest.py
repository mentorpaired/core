from ..models import RequestInterest
from ..serializers import RequestInterestSerializer
from .base import BaseTestCase


class TestRequestInterestViews(BaseTestCase):
    def test_get_all_interests(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token)
        response = self.client.get("/interests/")
        interests = RequestInterest.objects.all()
        serializer = RequestInterestSerializer(interests, many=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)

    def test_retrieve_valid_single_interest(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token)
        response = self.client.get(f"/interests/{self.request_interest.id}/")
        interest = RequestInterest.objects.get(id=self.request_interest.id)
        serializer = RequestInterestSerializer(interest)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)

    def test_retrieve_all_interests_linked_to_single_request(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token)
        response = self.client.get(f"/requests/{self.request.id}/interests/")
        self.assertEqual(response.status_code, 200)

    def test_retrieve_invalid_single_interest(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token)
        response = self.client.get("/interests/01/")
        self.assertEqual(response.status_code, 404)

    def test_can_create_new_interest(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token)
        response = self.client.post(
            "/interests/",
            {
                "request": self.request.id,
                "description": "Random description",
                "mentor": self.request_mentor.pk,
                "status": "OPEN",
            },
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(RequestInterest.objects.count(), 2)

    def test_cannot_create_invalid_interest(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token)
        response = self.client.post(
            "/interests/",
            {
                "request": "",
                "description": "Another random description",
                "mentor": "",
                "status": "OPEN",
            },
        )
        self.assertEqual(response.status_code, 400)

    def test_can_update_field_in_interest(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token)
        response = self.client.put(
            f"/interests/{self.request_interest.id}/",
            {"description": "Changed description"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["mentor"], self.profile.pk)
        self.assertEqual(response.data["description"], "Changed description")

    def test_can_delete_interest(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token)
        response = self.client.delete(f"/interests/{self.request_interest.id}/")
        self.assertEqual(response.status_code, 204)
