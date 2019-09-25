from django import forms
from django.forms import widgets
from webapp.models import Status, Type


class IssueForm(forms.Form):
    summary = forms.CharField(max_length=100, required=True, label='Summary')
    description = forms.CharField(max_length=3000, required=False, label='Description', widget=widgets.Textarea)
    create = forms.DateField(required=False, label='Date of create')
    status = forms.ModelChoiceField(queryset=Status.objects.all(), required=True, label='Status', empty_label="None")
    type = forms.ModelChoiceField(queryset=Type.objects.all(), required=True, label='Type', empty_label="None")


class StatusForm(forms.Form):
    status = forms.CharField(max_length=25, required=True, label='Status')


class TypeForm(forms.Form):
    type = forms.CharField(max_length=40, required=True, label='Type')


