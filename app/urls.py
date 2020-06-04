from django.urls import path

from .views.language import (LanguageDetail, LanguageList,
                             LanguageProficiencyDetail,
                             LanguageProficiencyList)
from .views.skill import (SkillDetail, SkillList, SkillProficiencyDetail,
                          SkillProficiencyList)
from .views.user import UserDetail, UserList
from .views.request import RequestDetail, RequestList

urlpatterns = [
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
