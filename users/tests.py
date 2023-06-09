from django.test import TestCase
from django.urls import reverse
from .models import CustomUser

from django.contrib.auth import get_user
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
        
        
        #
        second_response = self.client.get("/users/profile/defonic/")
        
        self.assertEqual(second_response.status_code, 200)
        
        
        ### login
        self.client.login(username = "defonic", password = "Pass!123")
        
        third_response = self.client.post(
            reverse("users:update"),
            data = {
                "username": "admin",
                "first_name": "admin",
                "last_name": "adminov",
                "email": "admin@admin.com",
                "phone": "+9989553255",
                "tg_username": "newusername",
                "avatar": "avatar.png",
                
            }
        )
        
        user = get_user(self.client)
        print(user.is_authenticated)
        
        self.assertEqual(third_response.status_code, 302)
        self.assertEqual(user.first_name, "admin")
        self.assertNotEqual(user.first_name, "Jaloliddin")
        self.assertEqual(user.email, "admin@admin.com")
        