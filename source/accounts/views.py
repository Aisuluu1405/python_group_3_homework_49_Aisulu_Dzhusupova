

from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import User
from django.http import request
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.views.generic import DetailView, UpdateView, ListView
from webapp.views.base_view import SessionUserMixin
from accounts.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from accounts.models import UserProfile


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = User(
                username=form.cleaned_data['username'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email']
            )
            user.set_password(form.cleaned_data['password'])
            user.save()
            UserProfile.objects.create(user=user)
            login(request, user)
            return redirect('webapp:index')
    else:
        form = UserCreationForm()
    return render(request, 'user_create.html', context={'form': form})


class UserDetailView(SessionUserMixin, DetailView):
    model = User
    template_name = 'user_detail.html'
    context_object_name = 'user_obj'

    def get(self, request, *args, **kwargs):
        self.set_request(request)
        self.page_login()
        return super().get(request, *args, **kwargs)


class UserInfoChangeView(UserPassesTestMixin, SessionUserMixin, UpdateView):
    model = User
    template_name = 'user_info_change.html'
    form_class = UserChangeForm
    context_object_name = 'user_obj'

    def get(self, request, *args, **kwargs):
        self.set_request(request)
        self.page_login()
        return super().get(request, *args, **kwargs)

    def test_func(self):
        return self.get_object() == self.request.user

    def get_success_url(self):
        return reverse('accounts:user_detail', kwargs={'pk':self.object.pk})


class UserPasswordChangeView(SessionUserMixin, UpdateView):
    model = User
    template_name = 'user_password_change.html'
    form_class = PasswordChangeForm
    context_object_name = 'user_obj'

    def get(self, request, *args, **kwargs):
        self.set_request(request)
        self.page_login()
        return super().get(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('accounts:login')


class UsersIndexView(SessionUserMixin, ListView):
    model = User
    template_name = 'users_index.html'
    context_object_name = 'users'

    def get(self, request, *args, **kwargs):
        self.set_request(request)
        self.page_login()
        return super().get(request, *args, **kwargs)


