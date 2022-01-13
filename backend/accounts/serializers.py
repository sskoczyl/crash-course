from rest_framework.serializers import ValidationError
from rest_framework import serializers

from django.db.utils import IntegrityError, DataError
from django.core.validators import EmailValidator
import django.contrib.auth.password_validation as validators

from .models import CustomUser


class RegistrationSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(
        write_only=True, required=True, validators=[EmailValidator]
    )
    password = serializers.CharField(write_only=True)
    display_name = serializers.CharField(required=False)

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

        try:
            account.save()
        except IntegrityError as error:
            raise ValidationError(detail={"email": ["Email is in use"]})
        except DataError as error:
            raise ValidationError(
                detail={"display_name": ["Display name can have max 30 characters"]}
            )

        return account
