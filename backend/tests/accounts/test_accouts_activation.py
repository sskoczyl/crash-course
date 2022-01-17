import email
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITransactionTestCase

from accounts.models import ActivationToken

User = get_user_model()


class AccountActivationTest(APITransactionTestCase):
    @classmethod
    def setUpClass(cls):
        cls.register_url = reverse("accounts:accounts_register")
        cls.user_data = {
            "email": "foobar@example.com",
            "password": "somepassword1",
            "display_name": "foobar",
        }

    def test_wrong_token(self):
        activate_url = reverse(
            "accounts:accounts_activate", kwargs={"token": "wrong-token"}
        )
        response = self.client.post(activate_url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_activation(self):
        self.client.post(self.register_url, self.user_data, format="json")

        user = User.objects.get(email=self.user_data.get("email"))
        token = ActivationToken.objects.get(user=user.id)

        self.assertFalse(user.is_active)
        self.assertEqual(ActivationToken.objects.count(), 1)

        activate_url = reverse(
            "accounts:accounts_activate", kwargs={"token": str(token)}
        )
        response = self.client.post(activate_url)

        user.refresh_from_db()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(user.is_active)
        self.assertEqual(ActivationToken.objects.count(), 0)

    def test_user_token_delete(self):
        self.client.post(self.register_url, self.user_data, format="json")

        user = User.objects.get(email=self.user_data.get("email"))
        token = ActivationToken.objects.get(user=user.id)

        self.assertEqual(ActivationToken.objects.count(), 1)

        user.delete()

        self.assertEqual(ActivationToken.objects.count(), 0)
