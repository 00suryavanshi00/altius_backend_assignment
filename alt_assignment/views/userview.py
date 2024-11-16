
from rest_framework import viewsets
from ..serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
# from drf_yasg.utils import swagger_auto_schema


class UserViewSet(viewsets.ViewSet):


    serializer_class = UserSerializer

    # @swagger_auto_schema(
    #     operation_description="User Sign up",
    #     security=[{'JWT': []}]  
    # )
    def create(self, request):

        password = request.data.get('password')
        password_confirmation = request.data.get('password_confirmation')

        if not password and not password_confirmation:

            return Response(
                {"error" : "Enter all the fields"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        if password != password_confirmation:

            return Response(
                {"error" : "Passwords don't match"},
                status=status.HTTP_400_BAD_REQUEST
            )
        

        serializer = UserSerializer(request.data)

        if serializer.is_valid():

            serializer.save()



