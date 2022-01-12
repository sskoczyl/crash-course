from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.core.validators import EmailValidator
import django.contrib.auth.password_validation as validators

from .models import CustomUser


class RegistrationSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=CustomUser.objects.all()), EmailValidator]
    )
    password = serializers.CharField(
        write_only=True,
    )
    display_name = serializers.CharField(required=False, max_length=32)

    class Meta:
        model = CustomUser
        fields = ("email", "password", "display_name")

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
