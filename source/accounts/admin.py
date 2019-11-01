from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from accounts.models import UserProfile


class ProfileInline(admin.StackedInline):
    model = UserProfile
    fields = ['about', 'avatar', 'github_profile']


class ProfileAdmin(UserAdmin):
    inlines = [ProfileInline]


admin.site.unregister(User)
admin.site.register(User, ProfileAdmin)
