from django.contrib import admin
from .models import User, Stack, SpokenLanguage, Request, InterestedMentor


# class UserAdmin (admin.ModelAdmin):
#     readonly_fields = ('user_id',)


# Add user admin function to registered user if need be
admin.site.register(User)
admin.site.register(Stack)
admin.site.register(SpokenLanguage)
admin.site.register(Request)
admin.site.register(InterestedMentor)
