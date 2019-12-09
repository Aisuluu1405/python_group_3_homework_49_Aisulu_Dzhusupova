from rest_framework import viewsets, generics
from webapp.models import Project, Issue
from api.serializers import ProjectSerializer, IssueSerializer
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


class IssueViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

