from django import forms

from webapp.models import Issue, Status, Type


class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        exclude = ['create']


class StatusForm(forms.ModelForm):
    class Meta:
        model= Status
        fields = ['status']


class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = ['type']
