from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class PasswordChangeTest(TestCase):
    def setUp(self):
        self.password = "Old-Strong-Password-123!"
        self.user = get_user_model().objects.create_user(
            username="testuser",
            password=self.password,
        )
        self.client.force_login(self.user)

    def test_password_change_page_loads(self):
        response = self.client.get(reverse("password_change"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/password_change_form.html")

    def test_password_change_success_redirects_to_done_page(self):
        new_password = "New-Strong-Password-456!"

        response = self.client.post(
            reverse("password_change"),
            {
                "old_password": self.password,
                "new_password1": new_password,
                "new_password2": new_password,
            },
        )

        self.assertRedirects(response, reverse("password_change_done"))

        self.user.refresh_from_db()
        self.assertTrue(self.user.check_password(new_password))

    def test_password_change_done_page_loads(self):
        response = self.client.get(reverse("password_change_done"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/password_change_done.html")
