from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


User = get_user_model()


class RegistrationTest(APITestCase):
    def test_create_user(self):
        data = {"email": "foobar@example.com", "password": "somepassword1", "display_name": "foobar"}

        response = self.client.post("/api/v1/accounts/register/", data, format="json")

        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, {
            "response": "Successfully registered",
            "email": "foobar@example.com",
            "display_name": "foobar"
        })

    def test_create_user_no_display_name(self):
        data = {"email": "foobar@example.com", "password": "somepassword1"}

        response = self.client.post("/api/v1/accounts/register/", data, format="json")

        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, {
            "response": "Successfully registered",
            "email": "foobar@example.com",
            "display_name": ""
        })

    def test_create_user_wrong_password(self):
        data = {"email": "foobar@example.com", "password": "s12", "display_name": "foobar"}

        response = self.client.post("/api/v1/accounts/register/", data, format="json")

        self.assertEqual(User.objects.count(), 0)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_create_user_occupied_email(self):
        data = {"email": "foobar@example.com", "password": "somepassword1"}
        response = self.client.post("/api/v1/accounts/register/", data, format="json")

        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        data = {"email": "foobar@example.com", "password": "somepassword1"}
        response = self.client.post("/api/v1/accounts/register/", data, format="json")

        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(response.status_code,  status.HTTP_400_BAD_REQUEST)


    def test_create_user_wrong_method(self):
        data = {"email": "foobar@example.com", "password": "somepassword1", "display_name": "foobar"}

        response = self.client.put("/api/v1/accounts/register/", data, format="json")

        self.assertEqual(User.objects.count(), 0)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)