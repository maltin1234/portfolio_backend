from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

class AuthenticationTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.email = 'jos@gmail.com'
        self.password = 'JonasJonas'

        # Create a test user with the specified email and password
        UserModel = get_user_model()
        self.user = UserModel.objects.create_user(email=self.email, password=self.password)
        
        # Debugging output to confirm user creation
        print(f"User created: {self.user.email}")

    def test_authenticate_user_with_email(self):
        """
        Test that an active user can authenticate using their email
        and receive a token.
        """
        # Prepare the data for the login request
        login_data = {
            'email': self.email,
            'password': self.password
        }
        
        # Send a POST request to obtain a token using email and password
        response = self.client.post(reverse('token_obtain_pair'), login_data)
        
        # Debugging output for response
        print(f"Response status: {response.status_code}, Response data: {response.data}")

        # Check if the response status is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Check if a token is returned in the response
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)
        
    def test_authenticate_user_with_invalid_email(self):
        """
        Test that authentication fails with an invalid email.
        """
        # Prepare data with an incorrect email
        login_data = {
            'email': 'invalid@example.com',
            'password': self.password
        }
        
        # Send a POST request to obtain a token
        response = self.client.post(reverse('token_obtain_pair'), login_data)
        
        # Check if the response status is 401 Unauthorized
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
        # Ensure no token is returned
        self.assertNotIn('access', response.data)
        
    def test_authenticate_user_with_wrong_password(self):
        """
        Test that authentication fails with an incorrect password.
        """
        # Prepare data with the correct email but incorrect password
        login_data = {
            'email': self.email,
            'password': 'wrongpassword'
        }
        
        # Send a POST request to obtain a token
        response = self.client.post(reverse('token_obtain_pair'), login_data)
        
        # Check if the response status is 401 Unauthorized
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
        # Ensure no token is returned
        self.assertNotIn('access', response.data)


#python manage.py test users.tests.login_test
