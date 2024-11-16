from rest_framework import serializers
from ..models import Profile


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ['id', 'name', 'profile_picture', 'bio']
        model = Profile