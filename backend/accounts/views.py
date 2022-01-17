from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from rest_framework.views import APIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework import status

from .serializers import RegistrationSerializer
from .models import ActivationToken, CustomUser


class UserRegister(CreateModelMixin, GenericViewSet):
    serializer_class = RegistrationSerializer
    activation_token_class = ActivationToken
    permission_classes = [~IsAuthenticated]

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        activation_token = self.activation_token_class.objects.create_token(user=user)
        print(
            "[USER ACTIVATION TOKEN] ", activation_token.get_token_value()
        )  # Temporary print

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserAccountActivation(APIView):
    activation_token_class = ActivationToken
    user_class = CustomUser
    permission_classes = [~IsAuthenticated]

    def post(self, request, *args, **kwargs):
        token_url_value = kwargs.get("token")

        try:
            token = self.activation_token_class.objects.get(value=token_url_value)
        except self.activation_token_class.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        if token.validate_token():
            user_to_activate = CustomUser.objects.get(id=token.user.id)
            user_to_activate.is_active = True
            user_to_activate.save(update_fields=["is_active"])

            token.delete()

            return Response(status=status.HTTP_200_OK)
        else:
            token.delete()

        return Response(status=status.HTTP_400_BAD_REQUEST)
