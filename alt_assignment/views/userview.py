from rest_framework import viewsets
from ..serializers import UserSerializer
from django.contrib.auth.models import User
from ..models import Profile
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
import os
from django.conf import settings


class UserViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

    @swagger_auto_schema(
        operation_description="Create a new user and default profile",
        request_body=UserSerializer,
        responses={
            201: openapi.Response("User created successfully with default profile"),
            400: "Bad Request - Missing or invalid fields",
        }
    )
    def create(self, request):
        password = request.data.get('password')
        password_confirmation = request.data.get('password_confirmation')
        email = request.data.get('email')

        if not password or not password_confirmation or not email:
            return Response(
                {"error": "Enter all the fields"},
                status=status.HTTP_400_BAD_REQUEST
            )

        if password != password_confirmation:
            return Response(
                {"error": "Passwords don't match"},
                status=status.HTTP_400_BAD_REQUEST
            )


        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():

            # hashing pass here
            user = User.objects.create_user(
                username=serializer.validated_data['username'],
                password=serializer.validated_data['password'],
                email=email
            )


            # now since a user is created ofc there will be a default profile for it
            # dummy image path
            dummy_img = os.path.join(settings.MEDIA_ROOT, 'dp.png') # excuse my handsome face :))

            # creating a default profile for the user
            Profile.objects.create(
                name=user.username,
                bio="",
                user=user,
                profile_picture=dummy_img if os.path.exists(dummy_img) else None #setting it to none if profile pic not found
            )

            return Response(
                {"message": "User created successfully with default profile"},
                status=status.HTTP_201_CREATED
            )
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
