from webapp.models import Project, Issue
from rest_framework import serializers

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'project', 'specification', 'date_create', 'date_update', 'status']

class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ['id', 'summary', 'description', 'status', 'type', 'project', 'create', 'update', 'created_by', 'assigned_to']