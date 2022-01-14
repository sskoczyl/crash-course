from rest_framework.serializers import ValidationError
from rest_framework import serializers

from django.db.utils import IntegrityError, DataError
from django.core.validators import EmailValidator
import django.contrib.auth.password_validation as validators

from .models import CustomUser


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("email", "password", "display_name")
        extra_kwargs = {
            "email": {"required": True, "write_only": True},
            "password": {"required": True, "write_only": True},
            "display_name": {"required": False, "write_only": True},
        }

    def validate_password(self, data):
        validators.validate_password(password=data, user=CustomUser)

        return data

    def save(self):
        account = CustomUser(
            email=self.validated_data["email"],
            display_name=self.validated_data.get("display_name"),
        )

        password = self.validated_data["password"]
        account.set_password(password)

        account.save()

        return account
