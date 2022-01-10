from rest_framework import serializers
from django.core.validators import EmailValidator
from rest_framework.validators import UniqueValidator


from .models import CustomUser

class RegistrationSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=CustomUser.objects.all()), EmailValidator]
    )
    password = serializers.CharField(min_length=8, write_only=True)
    display_name = serializers.CharField(required=False)

    class Meta:
        model = CustomUser
        fields = (
            "email",
            "password",
            "display_name"
        )

    def save(self):
        account = CustomUser(
            email = self.validated_data["email"]
        )

        if "display_name" in self.validated_data.keys():
            account.display_name = self.validated_data["display_name"]

        password = self.validated_data['password']
        account.set_password(password)
        account.save()

        return account
