from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.forms import ModelForm
from mailing.services import StyleFormMixin


class RegisterForm(StyleFormMixin, UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ["username", "email", "password1", "password2"]


class CustomUserModeratorForm(StyleFormMixin, ModelForm):
    class Meta:
        model = CustomUser
        fields = ["is_active"]


class CustomUserForm(StyleFormMixin, ModelForm):
    class Meta:
        model = CustomUser
        fields = ["username", "first_name", "last_name", "avatar", "phone_number", "country"]
