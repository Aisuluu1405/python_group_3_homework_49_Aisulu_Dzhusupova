# Generated by Django 2.2 on 2019-11-01 05:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': 'Profile', 'verbose_name_plural': 'Profiles'},
        ),
        migrations.AddField(
            model_name='userprofile',
            name='about',
            field=models.TextField(blank=True, null=True, verbose_name='About me'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='user_pics', verbose_name='User pic'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='github_profile',
            field=models.URLField(blank=True, null=True, verbose_name='GitHub Profile'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_profiles', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]
