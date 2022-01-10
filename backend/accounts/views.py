from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import RegistrationSerializer

class UserRegister(APIView):
    """
    Creates the user via registration.
    """
    def post(self, request, format="json"):
        serializer = RegistrationSerializer(data=request.data)
        data = {}

        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "Successfully registered"
            data['email'] = account.email
            data['display_name'] = account.display_name

            return Response(data, status=status.HTTP_201_CREATED)

        else:
            data = serializer.errors
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
