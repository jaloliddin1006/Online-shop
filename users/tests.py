from django.test import TestCase
from django.urls import reverse
from .models import CustomUser
# Create your tests here.



class SignupTestCase(TestCase):
    def test_signup_view(self):
        response = self.client.post(
            reverse("users:signup"),
            data = {
                "first_name": "Jaloliddin",
                "username": "defonic",
                "email": "123@admin.com",
                "password1": "Pass!123",
                "password2": "Pass!123",
            }
        )
        
        user = CustomUser.objects.get(username = "defonic")
        self.assertEqual(user.first_name, "Jaloliddin")
        self.assertEqual(user.email, "123@admin.com")
        self.assertTrue(user.check_password("Pass!123"))