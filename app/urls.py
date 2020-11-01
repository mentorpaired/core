"""
Urls
"""
from django.urls import path, include

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter

from .views.github_oauth import github_authenticate
from .views.language import LanguageViewSet, LanguageProficiencyViewSet
from .views.request import RequestDetail, RequestList
from .views.requests_interests import (
    MentorRequestInterest,
    RequestInterestDetail,
    RequestInterestList,
)
from .views.skill import SkillProficiencyViewSet, SkillViewSet
from .views.user import UserDetail, UserList

router = DefaultRouter()
router.register(r"languageproficiency", LanguageProficiencyViewSet)
router.register(r"languages", LanguageViewSet)
router.register(r"skillproficiency", SkillProficiencyViewSet)
router.register(r"skills", SkillViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("users/", UserList.as_view(), name="user_list"),
    path("users/<uuid:user_id>/", UserDetail.as_view(), name="user_detail"),
    path("github_auth/", github_authenticate),
    path("requests/", RequestList.as_view(), name="request_list"),
    path("requests/<int:request_id>/", RequestDetail.as_view(), name="request_detail"),
    path("interests/", RequestInterestList.as_view(), name="request_interest_list"),
    path(
        "interests/<int:interest_id>/",
        RequestInterestDetail.as_view(),
        name="request_interest_detail",
    ),
    path(
        "requests/<int:request_id>/interests/",
        MentorRequestInterest.as_view(),
        name="mentor_interest_detail",
    ),
]
