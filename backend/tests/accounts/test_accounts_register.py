from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITransactionTestCase

User = get_user_model()


class RegistrationTest(APITransactionTestCase):
    @classmethod
    def setUpClass(cls):
        cls.register_url = reverse("accounts:accounts_register")

    def test_create_user(self):
        data = {
            "email": "foobar@example.com",
            "password": "somepassword1",
            "display_name": "foobar",
        }
        response = self.client.post(self.register_url, data, format="json")

        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_user_no_display_name(self):
        data = {"email": "foobar@example.com", "password": "somepassword1"}
        response = self.client.post(self.register_url, data, format="json")

        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_user_too_short_password(self):
        data = {
            "email": "foobar@example.com",
            "password": "s12",
            "display_name": "foobar",
        }
        response = self.client.post(self.register_url, data, format="json")

        self.assertEqual(User.objects.count(), 0)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_occupied_email(self):
        data = {"email": "foobar@example.com", "password": "somepassword1"}
        response = self.client.post(self.register_url, data, format="json")

        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        data = {"email": "foobar@example.com", "password": "somepassword1"}
        response = self.client.post(self.register_url, data, format="json")

        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_no_email(self):
        data = {"email": "", "password": "somepassword1"}
        response = self.client.post(self.register_url, data, format="json")

        self.assertEqual(User.objects.count(), 0)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_wrong_method(self):
        data = {
            "email": "foobar@example.com",
            "password": "somepassword1",
            "display_name": "foobar",
        }
        response = self.client.put(self.register_url, data, format="json")

        self.assertEqual(User.objects.count(), 0)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
