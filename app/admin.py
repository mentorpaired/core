from django.contrib import admin
from .models import User, Stack, Spoken_Languages, Request, Interested_Mentor

# Register your models here.
admin.site.register(User)
admin.site.register(Stack)
admin.site.register(Spoken_Languages)
admin.site.register(Request)
admin.site.register(Interested_Mentor)
