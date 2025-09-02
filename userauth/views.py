from rest_framework import generics
from .serializers import RegisterSerializer
from django.contrib.auth.models import User

class RegisterView(generics.CreateAPIView):
    """
    API view for user registration.

    Accepts POST requests with username, email, and password.
    Returns the created user data (excluding password).
    """

    queryset = User.objects.all()
    serializer_class = RegisterSerializer