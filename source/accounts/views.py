from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from accounts.forms import UserCreationForm


def login_view(request):
    context = {}
    path_next = request.GET.get('next')
    path = request.session.setdefault('path', path_next)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if path:
                return redirect(path)
            return redirect('webapp:index')
        else:
            context['has_error'] = True
    return render(request, 'login.html', context=context)


def logout_view(request):
    logout(request)
    return redirect('webapp:index')
