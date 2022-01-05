from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin

from .serializers import RegistrationSerializer


class UserRegister(CreateModelMixin, GenericViewSet):
    serializer_class = RegistrationSerializer
    permission_classes = [~IsAuthenticated]
