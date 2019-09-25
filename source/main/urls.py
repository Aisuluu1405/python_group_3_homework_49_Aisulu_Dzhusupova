"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from webapp.views import IndexView, IssueView, IssueCreateView, issue_edit_view, issue_delete_view,\
    StatusIndexView, StatusCreateView, status_edit_view, status_delete_view,\
    TypeIndexView, TypeCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('issue/<int:pk>/', IssueView.as_view(), name='detail'),
    path('issue/add/', IssueCreateView.as_view(), name='issue_add'),
    path('issue/<int:pk>/edit/', issue_edit_view, name='issue_edit'),
    path('issue/delete/<int:pk>/', issue_delete_view, name='issue_delete'),
    path('status/', StatusIndexView.as_view(), name='status_index'),
    path('status/add/', StatusCreateView.as_view(), name='status_add'),
    path('status/<int:pk>/edit/', status_edit_view, name='status_edit'),
    path('status/delete/<int:pk>/', status_delete_view, name='status_delete'),
    path('type/', TypeIndexView.as_view(), name='type_index'),
    path('type/add/', TypeCreateView.as_view(), name='type_add'),
]
