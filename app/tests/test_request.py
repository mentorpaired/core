from ..models import Request
from ..serializers import RequestSerializer
from .base import BaseTestCase


class TestRequestViews(BaseTestCase):
    def test_get_all_requests(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token)
        response = self.client.get("/requests")
        requests = Request.objects.all()
        serializer = RequestSerializer(requests, many=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)

    def test_retrieve_valid_single_request(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token)
        response = self.client.get(f"/requests/{self.request.id}")
        request = Request.objects.get(id=self.request.id)
        serializer = RequestSerializer(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)

    def test_retrieve_invalid_single_request(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token)
        response = self.client.get("/requests/random_id")
        self.assertEqual(response.status_code, 404)

    def test_can_create_new_request(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token)
        response = self.client.post(
            "/requests",
            {
                "skill": [
                    self.beginner_python.id,
                ],
                "description": "Random description",
                "mentee": [
                    self.request_mentee.pk,
                ],
                "status": "OPEN",
            },
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Request.objects.count(), 2)

    def test_cannot_create_invalid_request(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token)
        response = self.client.post(
            "/requests",
            {
                "skill": "",
                "description": "Another random description",
                "mentee": "",
                "status": "OPEN",
            },
        )
        self.assertEqual(response.status_code, 400)

    def test_can_update_field_in_request(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token)
        response = self.client.put(
            f"/requests/{self.request.id}",
            {
                "skill": self.intermediate_python.id,
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["mentee"], self.request_mentee.pk)
        self.assertEqual(response.data["skill"], self.intermediate_python.id)

    def test_can_delete_request(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token)
        response = self.client.delete(f"/requests/{self.request.id}")
        self.assertEqual(response.status_code, 204)
