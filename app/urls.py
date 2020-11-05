from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views.github_oauth import github_authenticate
from .views.language import (
    LanguageDetail,
    LanguageList,
    LanguageProficiencyDetail,
    LanguageProficiencyList,
)
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
from .views.user import UserDetail, UserList

urlpatterns = [
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("skillproficiency/", SkillProficiencyList.as_view(), name="proficiency_list"),
    path(
        "skillproficiency/<int:pk>/",
        SkillProficiencyDetail.as_view(),
        name="proficiency_detail",
    ),
    path("skills/", SkillList.as_view(), name="skill_list"),
    path("skills/<int:pk>/", SkillDetail.as_view(), name="skill_list"),
    path(
        "languageproficiency/",
        LanguageProficiencyList.as_view(),
        name="languageproficiency_list",
    ),
    path(
        "languageproficiency/<int:pk>/",
        LanguageProficiencyDetail.as_view(),
        name="languageproficiency_detail",
    ),
    path("languages/", LanguageList.as_view(), name="language_list"),
    path("languages/<int:pk>/", LanguageDetail.as_view(), name="language_detail"),
    path("users/", UserList.as_view(), name="user_list"),
    path("users/<uuid:pk>/", UserDetail.as_view(), name="user_detail"),
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
