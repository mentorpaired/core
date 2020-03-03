from django.contrib import admin
from .models import User, Stack, SpokenLanguages, Request, InterestedMentor

# Register your models here.
admin.site.register(User)
admin.site.register(Stack)
admin.site.register(SpokenLanguages)
admin.site.register(Request)
admin.site.register(InterestedMentor)
