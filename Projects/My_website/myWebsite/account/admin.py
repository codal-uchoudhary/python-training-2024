from django.contrib import admin

from .models import UserContent, Profile


class PostAdmin(admin.ModelAdmin):
    admin.site.register(UserContent)
    admin.site.register(Profile)
