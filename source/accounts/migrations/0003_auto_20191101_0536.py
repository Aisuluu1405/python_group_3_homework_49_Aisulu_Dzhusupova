# Generated by Django 2.2 on 2019-11-01 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20191101_0520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='about',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='About me'),
        ),
    ]
