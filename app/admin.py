"""
Admin
"""
from django.contrib import admin

from .models import User, Skill, SpokenLanguage, Request, RequestInterest


admin.site.register(User)
admin.site.register(Skill)
admin.site.register(SpokenLanguage)
admin.site.register(Request)
admin.site.register(RequestInterest)
