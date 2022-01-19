from django.urls import path

from . import views

app_name = "accounts"

urlpatterns = [
    path(
        "register/",
        views.UserRegister.as_view({"post": "create"}),
        name="accounts_register",
    ),
    path(
        "activate/",
        views.UserAccountActivation.as_view(),
        name="accounts_activate",
    ),
]
