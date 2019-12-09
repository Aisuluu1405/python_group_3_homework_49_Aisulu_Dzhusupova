from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator

from webapp.models import Project, Issue
from rest_framework import serializers


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ['id', 'summary', 'description', 'status', 'type', 'project', 'create', 'update', 'created_by', 'assigned_to']


class ProjectSerializer(serializers.ModelSerializer):
    issues = IssueSerializer(many=True, read_only=True)
    date_create = serializers.DateTimeField(read_only=True)
    date_update = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'project', 'specification', 'date_create', 'date_update', 'status', 'issues']


class UserSerializer(serializers.ModelSerializer):

    def save(self, **kwargs):
        user = User(
            username = self.validated_data['username'],
            first_name = self.validated_data['first_name'],
            last_name = self.validated_data['last_name'],
            email = self.validated_data['email'])
        password = self.validated_data['password']
        print(password)
        user.set_password(password)
        user.save()
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password')