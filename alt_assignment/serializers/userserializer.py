from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True)


    class Meta:

        fields = [
            'id',
            'username',
            'password',
            'password_confirmation',
            'email'
        ]
        model = User


    def create(self, validated_data):

        validated_data.pop('password_confimation')
        user = User.objects.create_user(**validated_data)
        return user
