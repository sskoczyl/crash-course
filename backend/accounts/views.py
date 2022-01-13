from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from .serializers import RegistrationSerializer
from .tokens import account_activation_token
from .models import CustomUser


class UserRegister(CreateModelMixin, GenericViewSet):
    serializer_class = RegistrationSerializer
    permission_classes = [~IsAuthenticated]
