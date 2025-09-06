from rest_framework import generics

import userauth
from .models import AppUser
from .serializers import RegisterSerializer
from django.contrib.auth.models import User

class RegisterView(generics.CreateAPIView):
    """
    API view for user registration.

    Accepts POST requests with username, email, and password.
    Returns the created user data (excluding password).
    """

    queryset = AppUser.objects.all()
    serializer_class = RegisterSerializer