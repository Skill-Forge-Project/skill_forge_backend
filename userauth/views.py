from rest_framework import generics
from .models import AppUser
from .serializers import AppUserSerializer


class RegisterView(generics.CreateAPIView):
    """
    API view for user registration.

    Accepts POST requests with username, email, and password.
    Returns the created user data (excluding password).
    """

    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer
