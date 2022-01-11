from rest_framework import status
from rest_framework.response import Response
from django.http.response import HttpResponseRedirect
from rest_framework.views import APIView

from .serializers import RegistrationSerializer


class UserRegister(APIView):
    """
    Creates the user via registration.
    """

    def post(self, request):
        if not request.user.is_authenticated:
            serializer = RegistrationSerializer(data=request.data)
            data = {}

            if serializer.is_valid():
                account = serializer.save()
                data["response"] = "Successfully registered"
                data["email"] = account.email
                data["display_name"] = account.display_name

                return Response(data, status=status.HTTP_201_CREATED)

            else:
                data = serializer.errors
                return Response(data, status=status.HTTP_400_BAD_REQUEST)

        else:
            return HttpResponseRedirect(redirect_to="/")
