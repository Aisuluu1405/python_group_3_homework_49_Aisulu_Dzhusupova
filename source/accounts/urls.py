from django.urls import path
from accounts.views import login_view, logout_view, register_view, UserDetailView, UserInfoChangeView, UserPasswordChangeView, UsersIndexView

app_name = 'accounts'

urlpatterns = [
    path('accounts/login/', login_view, name='login'),
    path('accounts/logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('profile/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('profile/<int:pk>/edit/', UserInfoChangeView.as_view(), name = 'user_edit'),
    path('profile/<int:pk>/password_change/', UserPasswordChangeView.as_view(), name='password_change'),
    path('user/index', UsersIndexView.as_view(), name='users_index')
]

