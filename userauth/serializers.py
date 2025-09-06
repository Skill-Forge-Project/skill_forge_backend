from rest_framework import serializers
from userauth.models import AppUser

class AppUserSerializer(serializers.ModelSerializer):
    """
    Serializer for registering a new user.

    Validates and creates a new user using Django's built-in User model.
    Password is write-only and securely hashed before saving.
    """

    password = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = AppUser
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name', 'is_staff']
        read_only_fields = ['id', 'is_staff']
        
    def create(self, validated_data):
        user = AppUser(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
        