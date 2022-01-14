from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = (
        "email",
        "display_name",
        "is_active",
    )
    list_filter = (
        "email",
        "display_name",
        "is_active",
    )
    fieldsets = (
        (None, {"fields": ("email", "display_name", "password")}),
        ("Permissions", {"fields": ("is_active",)}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "display_name",
                    "password",
                    "is_active",
                ),
            },
        ),
    )
    search_fields = ("email", "display_name")
    ordering = ("email", "display_name")


admin.site.register(CustomUser, CustomUserAdmin)
