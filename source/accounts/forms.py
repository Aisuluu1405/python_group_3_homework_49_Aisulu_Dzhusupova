from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class UserCreationForm(forms.ModelForm):
    password = forms.CharField(label='Password', strip=False, widget=forms.PasswordInput)
    password_confirm =forms.CharField(label='Password Confirm', widget=forms.PasswordInput, strip=False)

    def clean_password_confirm(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Passwords do not match!')
        return password_confirm

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ['username', 'password', 'password_confirm', 'first_name', 'last_name', 'email']










