from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import AppUser

class RegistrationTestCase(APITestCase):
    """
    Test suite for AppUser registration endpoint.
    """

    def setUp(self):
        """
        Set up test data and endpoint URL.
        """
        self.register_url = reverse('register')
        self.user_data = {
            'email': 'test@example.com',
            'username': 'testuser',
            'password': 'securepassword123'
        }

    def test_user_registration(self):
        """
        Test successful registration of a new AppUser.
        """
        response = self.client.post(self.register_url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(AppUser.objects.count(), 1)
        self.assertEqual(AppUser.objects.get().email, 'test@example.com')
    
    def test_user_missing_email(self):
        """
        Test registration fails when email is missing.
        """
        data = self.user_data.copy()
        data.pop('email')
        response = self.client.post(self.register_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('email', response.data)
    
    def test_user_missing_username(self):
        """
        Test registration fails when username is missing.
        """
        data = self.user_data.copy()
        data.pop('username')
        response = self.client.post(self.register_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('username', response.data)
    
    def test_user_missing_password(self):
        """
        Test registration fails when password is missing.
        """
        data = self.user_data.copy()
        data.pop('password')
        response = self.client.post(self.register_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('password', response.data)