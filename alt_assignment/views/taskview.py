

from ..serializers import TaskSerializer
from ..models import Task
from rest_framework import viewsets
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated

class TaskViewSet(viewsets.ModelViewSet):

    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]


    @swagger_auto_schema(
        operation_description="Gets all the user tasks",
        security=[{'JWT': []}]  
    )
    def get_queryset(self):
        Task.objects.get(user = self.request.user)

    
    @swagger_auto_schema(
        operation_description="Create tasks",
        security=[{'JWT': []}]  
    )
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)
    