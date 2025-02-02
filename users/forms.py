from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.forms import ModelForm


class RegisterForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ["username", "email", "password1", "password2"]


class CustomUserModeratorForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ["is_active"]


class CustomUserForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ["username", "first_name", "last_name"]
