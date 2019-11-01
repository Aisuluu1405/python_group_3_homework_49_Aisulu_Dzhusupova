from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='user_profiles', on_delete=models.CASCADE)
    github_profile = models.CharField(max_length=200, blank=True, verbose_name='GitHub Profile')

    def __str__(self):
        return self.github_profile


