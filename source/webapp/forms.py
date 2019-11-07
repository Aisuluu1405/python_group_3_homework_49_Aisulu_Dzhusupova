from django import forms
from django.contrib.auth.models import User

from webapp.models import Issue, Status, Type, Project


class IssueForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user_projects = kwargs.pop('current_project')
        super().__init__(*args, **kwargs)
        self.fields['assigned_to'].queryset = User.objects.filter(user_team__project__in=self.user_projects).distinct()

    class Meta:
        model = Issue
        exclude = ['create', 'project', 'created_by']


class StatusForm(forms.ModelForm):
    class Meta:
        model= Status
        fields = ['status']


class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = ['type']


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['date_create', 'date_update']


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label='Search')
