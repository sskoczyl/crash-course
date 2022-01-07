from rest_framework import serializers
from .models import CustomUser

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "email",
            "password",
            "display_name",
        ]

        extra_kwargs = {
            "password": {"write_only": True}
        }

    def save(self):
        account = CustomUser(
            email = self.validated_data['email'],
            display_name = self.validated_data['display_name']
        )
        password = self.validated_data['password']
        
        # VALIDATOR FOR PASSWORD AND MAIL!

        account.set_password(password)
        account.save()

        return account