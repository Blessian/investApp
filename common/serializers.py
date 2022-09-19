from rest_framework import serializers

from .models import User


class UserCreateSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )
        return user

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'is_staff']
        read_only_fields = ['is_staff']
        extra_kwargs = {
            'password': {'write_only': True}
        }
