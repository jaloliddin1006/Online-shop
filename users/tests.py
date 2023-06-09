from django.test import TestCase
from django.urls import reverse
from .models import CustomUser

from django.contrib.auth import get_user
# Create your tests here.



class SignupTestCase(TestCase):
    ### signup test | ma'lumot kiritish
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
         ## kiritilgan ma'lumotni olib tekshirib korish
        user = CustomUser.objects.get(username = "defonic")
        self.assertEqual(user.first_name, "Jaloliddin")
        self.assertEqual(user.email, "123@admin.com")
        self.assertTrue(user.check_password("Pass!123"))
        
        
        ### profil ( get) funksiyasini tekshirish
        second_response = self.client.get("/users/profile/defonic/")
        
        self.assertEqual(second_response.status_code, 200)
        
        
        ### tizimga login
        self.client.login(username = "defonic", password = "Pass!123")
        
        ## profil ma'lumotlarini yangilash funksiyani tekshirish
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
        
        ## yangilangan userni ma'lumotlarini olish
        user = get_user(self.client)
        # yangilangan userning datalarining yangilanganligini tekshirish
        self.assertEqual(third_response.status_code, 302)
        self.assertEqual(user.first_name, "admin")
        self.assertNotEqual(user.first_name, "Jaloliddin")
        self.assertEqual(user.email, "admin@admin.com")
        