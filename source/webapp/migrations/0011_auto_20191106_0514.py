# Generated by Django 2.2 on 2019-11-06 05:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0010_auto_20191103_0748'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='team',
            options={'verbose_name': 'Team', 'verbose_name_plural': 'Teams'},
        ),
        migrations.AddField(
            model_name='issue',
            name='assigned_to',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='issues_perfomer', to=settings.AUTH_USER_MODEL, verbose_name='Issue perfomer'),
        ),
        migrations.AddField(
            model_name='issue',
            name='created_by',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='issues_author', to=settings.AUTH_USER_MODEL, verbose_name='Issue author'),
        ),
    ]
