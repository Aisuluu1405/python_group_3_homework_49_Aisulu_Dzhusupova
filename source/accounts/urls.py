from django.urls import path
from accounts.views import login_view, logout_view

app_name = 'accounts'

urlpatterns = [
    path('accounts/login/', login_view, name='login'),
    path('accounts/logout/', logout_view, name='logout')
]
