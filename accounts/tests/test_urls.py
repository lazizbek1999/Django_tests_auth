from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
class TestUrls(TestCase):
    
    def test_urls(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)     
        self.assertTemplateUsed(response, 'registration/signup.html')
       
    def test_login_page_loads(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')
        
    def test_signup_form(self):
        response = self.client.post(
            reverse('signup'),
            {
                'username': 'Lazizbek',
                'email': 'AdminCraft@gmail.com',
                'password1': 'Warsaw2026',
                'password2': 'Warsaw2026',
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username,'Lazizbek')
        self.assertEqual(get_user_model().objects.all()[0].email,'AdminCraft@gmail.com')
        self.assertTrue(get_user_model().objects.all()[0].check_password('Warsaw2026'))
        