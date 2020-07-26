from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from .views.github_auth import GithubAuthView, GithubUser
from .views.language import (LanguageDetail, LanguageList,
                             LanguageProficiencyDetail,
                             LanguageProficiencyList)
from .views.request import RequestDetail, RequestList
from .views.skill import (SkillDetail, SkillList, SkillProficiencyDetail,
                          SkillProficiencyList)
from .views.user import UserDetail, UserList

urlpatterns = [
    path(
        'api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'
    ),
    path(
        'api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'
    ),
    path(
        'github_oauth/', GithubAuthView.as_view(), name='github_oauth'
    ),
    path(
        'github_user/<str:token>/', GithubUser.as_view(), name='github_user'
    ),
    path(
        'skillproficiency/',
        SkillProficiencyList.as_view(),
        name='proficiency_list'
    ),
    path(
        'skillproficiency/<int:pk>/',
        SkillProficiencyDetail.as_view(),
        name='proficiency_detail'
    ),
    path(
        'skills/',
        SkillList.as_view(),
        name='skill_list'
    ),
    path(
        'skills/<int:pk>/',
        SkillDetail.as_view(),
        name='skill_list'
    ),
    path(
        'languageproficiency/',
        LanguageProficiencyList.as_view(),
        name='languageproficiency_list'
    ),
    path(
        'languageproficiency/<int:pk>/',
        LanguageProficiencyDetail.as_view(),
        name='languageproficiency_detail'
    ),
    path(
        'languages/',
        LanguageList.as_view(),
        name='language_list'
    ),
    path(
        'languages/<int:pk>/',
        LanguageDetail.as_view(),
        name='language_detail'
    ),
    path(
        'users/',
        UserList.as_view(),
        name='user_list'
    ),
    path(
        'users/<uuid:pk>/',
        UserDetail.as_view(),
        name='user_detail'
    ),
    path(
        'requests/',
        RequestList.as_view(),
        name='request_list'
    ),
    path(
        'requests/<int:pk>/',
        RequestDetail.as_view(),
        name='request_detail'
    )
]
