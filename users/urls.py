from django.urls import path, reverse_lazy
from django.contrib.auth.views import (LoginView, LogoutView, PasswordResetView, PasswordResetDoneView,
                                       PasswordResetConfirmView, PasswordResetCompleteView)
from django.views.decorators.cache import cache_page
from .views import RegisterView, CustomUserListView, CustomUserUpdateView, ProfileView
from .apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
    path("login/", cache_page(60)(LoginView.as_view()), name="login"),
    path("logout/", LogoutView.as_view(template_name="registration/logout.html"), name="logout"),
    path("register/", cache_page(60)(RegisterView.as_view()), name="register"),

    path("user_list/", CustomUserListView.as_view(), name="user_list"),
    path("user_update/<int:pk>", CustomUserUpdateView.as_view(), name="user_update"),

    path("profile/<int:pk>/", ProfileView.as_view(), name="profile"),

    path("password_reset/",
         PasswordResetView.as_view(
             template_name="password_reset/password_reset_form.html",
             success_url=reverse_lazy("users:password_reset_done"),
             email_template_name="password_reset/password_reset_email.html"),
         name="password_reset"
         ),
    path("password_reset_done/",
         PasswordResetDoneView.as_view(
             template_name="password_reset/password_reset_done.html"),
         name="password_reset_done"
         ),
    path("password_reset_confirm/<uidb64>/<token>/",
         PasswordResetConfirmView.as_view(
             template_name="password_reset/password_reset_confirm.html",
             success_url=reverse_lazy("users:password_reset_complete")),
         name="password_reset_confirm"
         ),
    path("password_reset_complete/",
         PasswordResetCompleteView.as_view(
             template_name="password_reset/password_reset_complete.html"),
         name="password_reset_complete"
         ),
]
