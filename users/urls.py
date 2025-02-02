from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import RegisterView, CustomUserListView, CustomUserUpdateView
from .apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(template_name="registration/logout.html"), name="logout"),
    path("register/", RegisterView.as_view(), name="register"),

    path("user_list/", CustomUserListView.as_view(), name="user_list"),
    path("user_update/<int:pk>", CustomUserUpdateView. as_view(), name="user_update"),
]
