from django.views.generic import CreateView, ListView, UpdateView, TemplateView
from .forms import RegisterForm, CustomUserModeratorForm, CustomUserForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import CustomUser


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("users:login")


class CustomUserListView(LoginRequiredMixin, ListView):
    model = CustomUser


class CustomUserUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = CustomUserModeratorForm
    success_url = reverse_lazy("users:user_list")

    def get_form_class(self):
        if self.request.user.pk == self.object.pk:
            return CustomUserForm
        elif self.request.user.has_perm("can_block_user"):
            return CustomUserModeratorForm


class ProfileView(TemplateView):

    template_name = "users/profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["username"] = CustomUser.username
        context["first_name"] = CustomUser.first_name
        context["last_name"] = CustomUser.last_name
        context["email"] = CustomUser.email
        context["phone_number"] = CustomUser.phone_number
        context["country"] = CustomUser.country
        context["avatar"] = CustomUser.avatar
        return context
