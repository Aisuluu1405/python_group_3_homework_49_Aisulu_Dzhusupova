# Generated by Django 2.2 on 2019-10-09 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_auto_20191008_0323'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('closed', 'Сlosed')], default='active', max_length=20, verbose_name='Status'),
        ),
    ]
