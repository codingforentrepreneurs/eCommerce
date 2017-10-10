from django.contrib import admin

from .models import ObjectViewed, UserSession


admin.site.register(ObjectViewed)

admin.site.register(UserSession)