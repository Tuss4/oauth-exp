from rest_framework import serializers
from .models import User


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'email', 'created', 'password')
        read_only_fields = ('id', 'created')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 8}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
