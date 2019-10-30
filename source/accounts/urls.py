from django.urls import path
from accounts.views import register_view, UserDetailView, UserInfoChangeView, UserPasswordChangeView, UsersIndexView
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'accounts'

urlpatterns = [
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('register/', register_view, name='register'),
    path('profile/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('profile/<int:pk>/edit/', UserInfoChangeView.as_view(), name = 'user_edit'),
    path('profile/<int:pk>/password_change/', UserPasswordChangeView.as_view(), name='password_change'),
    path('user/index', UsersIndexView.as_view(), name='users_index')
]

