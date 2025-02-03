from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.views.decorators.cache import cache_page
from .views import RegisterView, CustomUserListView, CustomUserUpdateView, ProfileView
from .apps import UsersConfig


app_name = UsersConfig.name

urlpatterns = [
    path("login/", cache_page(60)(LoginView.as_view()), name="login"),
    path("logout/", LogoutView.as_view(template_name="registration/logout.html"), name="logout"),
    path("register/", cache_page(60)(RegisterView.as_view()), name="register"),

    path("user_list/", CustomUserListView.as_view(), name="user_list"),
    path("user_update/<int:pk>", CustomUserUpdateView. as_view(), name="user_update"),

    path("profile/<int:pk>/", ProfileView.as_view(), name="profile"),
]
