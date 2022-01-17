from typing import overload
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework import status

from .serializers import RegistrationSerializer
from .models import ActivationToken


class UserRegister(CreateModelMixin, GenericViewSet):
    serializer_class = RegistrationSerializer
    activation_token_class = ActivationToken
    permission_classes = [~IsAuthenticated]

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        print(activation_token_class.)

        return Response(serializer.data, status=status.HTTP_201_CREATED)