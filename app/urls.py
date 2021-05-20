from django.urls import path, include

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views.github_oauth import github_authenticate
from .views.gitlab_oauth import gitlab_authenticate

from .views.goal import GoalViewSet, RetrieveUserGoal

from .views.language import (
    LanguageDetail,
    LanguageList,
    LanguageProficiencyDetail,
    LanguageProficiencyList,
)

from .views.role import RoleList, RoleDetail

from .views.request import RequestDetail, RequestList

from .views.requests_interests import (
    MentorRequestInterest,
    RequestInterestDetail,
    RequestInterestList,
)
from .views.skill import (
    SkillDetail,
    SkillList,
    SkillProficiencyDetail,
    SkillProficiencyList,
)
from .views.user import UserDetail, UserList, MentorUserList

schema_view = get_schema_view(
    openapi.Info(
        title="MentorPaired API",
        default_version="v1",
        description="MentorPaired's API Documentation",
        contact=openapi.Contact(email="mentorpaired@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

router = DefaultRouter()
router.register(r"goals", GoalViewSet, basename="goals")

urlpatterns = [
    path("", include(router.urls)),
    path("api/token", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh", TokenRefreshView.as_view(), name="token_refresh"),
    path(
        "api/mentorpaired/docs",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("skillproficiency", SkillProficiencyList.as_view(), name="proficiency_list"),
    path(
        "skillproficiency/<int:pk>",
        SkillProficiencyDetail.as_view(),
        name="proficiency_detail",
    ),
    path("skills", SkillList.as_view(), name="skill_list"),
    path("skills/<int:pk>", SkillDetail.as_view(), name="skill_list"),
    path(
        "languageproficiency",
        LanguageProficiencyList.as_view(),
        name="languageproficiency_list",
    ),
    path(
        "languageproficiency/<int:pk>",
        LanguageProficiencyDetail.as_view(),
        name="languageproficiency_detail",
    ),
    path("languages", LanguageList.as_view(), name="language_list"),
    path("languages/<int:pk>", LanguageDetail.as_view(), name="language_detail"),
    path("users", UserList.as_view(), name="user_list"),
    path("users/<uuid:pk>", UserDetail.as_view(), name="user_detail"),
    path("mentors", MentorUserList.as_view(), name="mentor_user"),
    path("github_auth", github_authenticate),
    path("gitlab_auth", gitlab_authenticate),
    path("requests", RequestList.as_view(), name="request_list"),
    path("requests/<int:id_>", RequestDetail.as_view(), name="request_detail"),
    path("interests", RequestInterestList.as_view(), name="request_interest_list"),
    path(
        "interests/<int:id_>",
        RequestInterestDetail.as_view(),
        name="request_interest_detail",
    ),
    path(
        "requests/<int:id_>/interests",
        MentorRequestInterest.as_view(),
        name="mentor_interest_detail",
    ),
    path("users/<uuid:pk>/goals", RetrieveUserGoal.as_view(), name="users_goals"),
    path("roles", RoleList.as_view(), name="role_list"),
    path("roles/<int:pk>", RoleDetail.as_view(), name="role_detail"),
]
