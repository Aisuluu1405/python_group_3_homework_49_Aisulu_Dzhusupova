from django.urls import include, path
from rest_framework import routers
from api.views import ProjectViewSet, IssueViewSet, RegisterView
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'issues', IssueViewSet)

app_name = 'api'

urlpatterns =[
    path('', include(router.urls)),
    path('login/', obtain_auth_token, name='api_token_auth'),
    path('register/', RegisterView.as_view(), name='user_register'),

]