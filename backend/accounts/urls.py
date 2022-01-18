from django.urls import path

from rest_framework_simplejwt import views as jwt_views

from . import views

app_name = "accounts"

urlpatterns = [
    path(
        "register/",
        views.UserRegister.as_view({"post": "create"}),
        name="accounts_register",
    ),
    path(
        "activate/<slug:token>/",
        views.UserAccountActivation.as_view(),
        name="accounts_activate",
    ),
    path(
        "token/",
        jwt_views.TokenObtainPairView.as_view(),
        name="accounts_jwt",
    ),
    path(
        "token/refresh/",
        jwt_views.TokenRefreshView.as_view(),
        name="accounts_jwt_refresh",
    ),
    path('hello/', views.HelloView.as_view(), name='hello'),
]
