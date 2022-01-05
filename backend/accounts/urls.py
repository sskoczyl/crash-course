from django.urls import path

from .views import registration_view, test

app_name = "accounts"

urlpatterns = [
    path('register/', registration_view, name="register"),
    path('test/', test, name="test"),
]
