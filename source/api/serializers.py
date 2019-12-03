from webapp.models import Project, Issue
from rest_framework import serializers

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'project', 'specification', 'date_create', 'date_update', 'status']

