

from ..serializers import ProfileSerializer
from ..models import Profile
from rest_framework import viewsets
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User
from drf_yasg import openapi
from rest_framework.response import Response

class ProfileViewSet(viewsets.ViewSet):

    serializer_class = ProfileSerializer
    permission_classes = [AllowAny]


    @swagger_auto_schema(
        operation_description="Gets User Profile based on email",
        responses={
            200: openapi.Response("Fetched profiles"),
            400: "Bad Request - Missing or invalid fields",
        },
        manual_parameters=[
            openapi.Parameter(
                'email', openapi.IN_QUERY, description="Email of the user to fetch profile", type=openapi.TYPE_STRING
            ),
        ]
    )
    def list(self, request):
        email = self.request.query_params.get('email')

        if email:
            try:
                user = User.objects.get(email=email)
                profiles = Profile.objects.filter(user=user)
                serializer = ProfileSerializer(profiles, many=True)
                return Response(serializer.data)
            except User.DoesNotExist:
                return Response({"error": "User not found"}, status=400)
        else:
            return Response({"error": "Email param missing"}, status=400)

    

    @swagger_auto_schema(
        operation_description="Creates profile",
        security=[{'JWT': []}]  
    )
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)
    