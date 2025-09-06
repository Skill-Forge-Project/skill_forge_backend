from django.contrib.auth.models import User
from rest_framework import serializers

from userauth.models import AppUser


class RegisterSerializer(serializers.ModelSerializer):
    """
    Serializer for registering a new user.

    Validates and creates a new user using Django's built-in User model.
    Password is write-only and securely hashed before saving.
    """

    password = serializers.CharField(write_only=True)

    class Meta:
        model = AppUser
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        """
        Create and return a new User instance, given the validated data.

        Args:
            validated_data (dict): Dictionary containing username, email, and password.

        Returns:
            User: A newly created User object.
        """
        user = AppUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user