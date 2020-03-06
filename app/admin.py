from django.contrib import admin
from .models import User, Stack, SpokenLanguages, Request, InterestedMentor


class UserAdmin (admin.ModelAdmin):
    readonly_fields = ('user_id',)


admin.site.register(User, UserAdmin)
admin.site.register(Stack)
admin.site.register(SpokenLanguages)
admin.site.register(Request)
admin.site.register(InterestedMentor)
