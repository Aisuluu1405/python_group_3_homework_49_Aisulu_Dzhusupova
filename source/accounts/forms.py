from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class UserCreationForm(forms.ModelForm):
    password = forms.CharField(label='Password', strip=False, widget=forms.PasswordInput)
    password_confirm = forms.CharField(label='Password Confirm', widget=forms.PasswordInput, strip=False)
    email = forms.EmailField(label='Email', required=True)

    def clean(self):
        super().clean()
        data = self.cleaned_data
        if not data.get('first_name') and not data.get('last_name'):
            raise ValidationError(
                '*Field "First name" or "Last name" should not be empty!',
                code='first_name_last_name_criteria_empty'
            )
        return data

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

    def clean_username(self):
        username = self.cleaned_data.get('username')
        try:
            User.objects.get(username=username)
            raise ValidationError('User with this username already exists',
                                  code = 'user_username_exists')
        except User.DoesNotExist:
            return username

    class Meta:
        model = User
        fields = ['username', 'password', 'password_confirm', 'first_name', 'last_name', 'email']


class UserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        labels = {'first_name': 'First name', 'last_name': 'Last name', 'email': 'Email'}


class PasswordChangeForm(forms.ModelForm):
    password = forms.CharField(label='New Password', strip=False, widget=forms.PasswordInput)
    password_confirm = forms.CharField(label='Confirm new Password', widget=forms.PasswordInput, strip=False)
    old_password = forms.CharField(label='Old Password', strip=False, widget=forms.PasswordInput)

    def clean_password_confirm(self):
        password = self.cleaned_data.get("password")
        password_confirm = self.cleaned_data.get("password_confirm")
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Passwords do not match!')
        return password_confirm

    def clean_old_password(self):
        old_password = self.cleaned_data.get("old_password")
        if not self.instance.check_password(old_password):
            raise forms.ValidationError('Old password is incorrect!')
        return old_password

    def save(self, commit=True):
        user = self.instance
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ['password', 'password_confirm', 'old_password']





