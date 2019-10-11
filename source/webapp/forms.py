from django import forms

from webapp.models import Issue, Status, Type, Project


class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        exclude = ['create', 'project']


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
