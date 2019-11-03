from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='user_profiles', on_delete=models.CASCADE, verbose_name='User')
    about = models.TextField(max_length=1000, null=True, blank=True, verbose_name='About me')
    avatar = models.ImageField(null=True, blank=True, upload_to='user_pics', verbose_name='User pic')
    github_profile = models.URLField(max_length=200, null=True, blank=True, verbose_name='GitHub Profile')

    def __str__(self):
        return self.user.get_full_name() + "'s Profile"

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

