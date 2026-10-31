from django.contrib.auth import get_user_model
from django.test import TestCase


class UserManagerTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="Lazizbek",
            email="Lazizbek1999@gmail.com",
            password="1999Lazizbek",
        )
        self.assertEqual(user.username, "Lazizbek")
        self.assertEqual(user.email, "Lazizbek1999@gmail.com")
        self.assertTrue(user.check_password("1999Lazizbek"))
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)


    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username="testsuperuser",
            email="testsuperuser@example.com",
            password="testpass1234",
        )
        self.assertEqual(admin_user.username, "testsuperuser")
        self.assertEqual(admin_user.email, "testsuperuser@example.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
