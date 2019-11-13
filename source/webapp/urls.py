from django.urls import path
from webapp.views import IndexView, IssueView, IssueCreateView, IssueEditView, IssueDeleteView, IssueProjectCreateView,\
    StatusIndexView, StatusCreateView, StatusEditView, StatusDeleteView,\
    TypeIndexView, TypeCreateView, TypeEditView, TypeDeleteView,\
    ProjectIndexView, ProjectView, ProjectCreateView, ProjectEditView, ProjectDeleteView, ProjectIndexNewView,\
    ProjectNewView, ProjectNewDeleteView

app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('issue/<int:pk>/', IssueView.as_view(), name='detail'),
    path('issue/add/', IssueCreateView.as_view(), name='issue_add'),
    path('issue/<int:pk>/edit/', IssueEditView.as_view(), name='issue_edit'),
    path('issue/delete/<int:pk>/', IssueDeleteView.as_view(), name='issue_delete'),
    path('status/', StatusIndexView.as_view(), name='status_index'),
    path('status/add/', StatusCreateView.as_view(), name='status_add'),
    path('status/<int:pk>/edit/', StatusEditView.as_view(), name='status_edit'),
    path('status/delete/<int:pk>/', StatusDeleteView.as_view(), name='status_delete'),
    path('type/', TypeIndexView.as_view(), name='type_index'),
    path('type/add/', TypeCreateView.as_view(), name='type_add'),
    path('type/<int:pk>/edit/', TypeEditView.as_view(), name='type_edit'),
    path('type/delete/<int:pk>/', TypeDeleteView.as_view(), name='type_delete'),
    path('project/', ProjectIndexView.as_view(), name='project_index'),
    path('project/<int:pk>/', ProjectView.as_view(), name='project_detail'),
    path('project/add/', ProjectCreateView.as_view(), name='project_add'),
    path('project/<int:pk>/edit/', ProjectEditView.as_view(), name='project_edit'),
    path('project/delete/<int:pk>/', ProjectDeleteView.as_view(), name='project_delete'),
    path('project/<int:pk>/add_issue/', IssueProjectCreateView.as_view(), name='project_issue_add'),
    path('project_new/', ProjectIndexNewView.as_view(), name='project_new_index'),
    path('project_new/<int:pk>/', ProjectNewView.as_view(), name='project_new_detail'),
    path('project_new/delete/<int:pk>', ProjectNewDeleteView.as_view(), name='project_new_delete'),

]