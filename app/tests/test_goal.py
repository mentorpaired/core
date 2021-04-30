import json

from ..models import Goal
from ..serializers import GoalSerializer
from .base import BaseTestCase


class TestGoalsView(BaseTestCase):
    def test_get_all_goals(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token)
        response = self.client.get("/goals/")
        goals = Goal.objects.all()
        serializer = GoalSerializer(goals, many=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)

    def test_retrieve_valid_single_goal(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token)
        response = self.client.get(f"/goals/{self.goal.id}/")
        goal = Goal.objects.get(id=self.goal.id)
        serializer = GoalSerializer(goal)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)

    def test_retrieve_invalid_single_goal(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token)
        response = self.client.get("/goals/random_id/")
        self.assertEqual(response.status_code, 404)

    def test_can_create_new_goal(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token)
        response = self.client.post(
            "/goals/",
            {
                "user": [
                    self.admin,
                ],
                "goal": "Learn Go",
                "description": "Need a mentor, want to learn the advanced topics of Go.",
            },
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Goal.objects.count(), 2)

    def test_second_admin_cannot_update_field_in_base_goal_object(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.second_token)
        response = self.client.put(
            f"/goals/{self.goal.id}/",
            {
                "goal": "Learn Python",
            },
        )
        self.assertEqual(response.status_code, 403)
        self.assertEqual(
            json.loads(response.content),
            {"detail": "You do not have permission to perform this action."},
        )

    def test_admin_can_update_field_in_base_goal_object(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token)
        response = self.client.put(
            f"/goals/{self.goal.id}/",
            {
                "goal": "Learn Python",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["goal"], "Learn Python")

    def test_second_admin_cannot_delete_base_goal(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.second_token)
        response = self.client.delete(f"/goals/{self.goal.id}/")
        self.assertEqual(response.status_code, 403)

    def test_admin_can_delete_gial(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token)
        response = self.client.delete(f"/goals/{self.goal.id}/")
        self.assertEqual(response.status_code, 204)
