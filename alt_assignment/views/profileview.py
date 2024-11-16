

from ..serializers import ProfileSerializer
from ..models import Profile
from rest_framework import viewsets
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated

class ProfileViewSet(viewsets.ViewSet):

    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]


    @swagger_auto_schema(
        operation_description="Gets user profile",
        security=[{'JWT': []}]  
    )
    def get_queryset(self):
        Profile.objects.get(user = self.request.user)

    

    @swagger_auto_schema(
        operation_description="Creates profile",
        security=[{'JWT': []}]  
    )
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)
    