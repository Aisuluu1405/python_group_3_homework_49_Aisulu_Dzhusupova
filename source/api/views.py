from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from webapp.models import Project, Issue
from api.serializers import ProjectSerializer, IssueSerializer, UserSerializer
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly, AllowAny


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


class IssueViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


class RegisterView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)

