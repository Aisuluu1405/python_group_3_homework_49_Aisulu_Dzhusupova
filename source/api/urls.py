from django.urls import include, path
from rest_framework import routers
from api.views import ProjectViewSet, IssueViewSet

router = routers.DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'issues', IssueViewSet)

app_name = 'api'

urlpatterns =[
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]