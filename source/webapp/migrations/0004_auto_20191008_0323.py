# Generated by Django 2.2 on 2019-10-08 03:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20190926_0852'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.CharField(max_length=100, verbose_name='Project')),
                ('specification', models.TextField(blank=True, max_length=3500, null=True, verbose_name='Specification')),
                ('date_create', models.DateTimeField(auto_now_add=True, verbose_name='Create project')),
                ('date_update', models.DateTimeField(auto_now=True, verbose_name='Update project')),
            ],
        ),
        migrations.AddField(
            model_name='issue',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='issues', to='webapp.Project', verbose_name='Project'),
        ),
    ]