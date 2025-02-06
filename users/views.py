from django.contrib.auth import login
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.generic import CreateView, ListView, UpdateView, TemplateView, View
from .forms import RegisterForm, CustomUserModeratorForm, CustomUserForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import CustomUser
from django.contrib.auth.tokens import PasswordResetTokenGenerator, default_token_generator
import os


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = "registration/register.html"

    def form_valid(self, form):
        # отправка ссылки подтверждения
        user = form.save()
        email = user.email
        token = default_token_generator.make_token(user)
        uemail = urlsafe_base64_encode(force_bytes(email))
        activation_url = reverse_lazy('users:confirm_email', kwargs={'uemailb64': uemail, 'token': token})
        # current_site = Site.objects.get_current().domain
        send_mail(
            'Подтвердите свой электронный адрес',
            f'Пожалуйста, перейдите по следующей ссылке, чтобы подтвердить свой адрес электронной почты: '
            f'http://127.0.0.1:8000{activation_url}',
            from_email=os.getenv("EMAIL_HOST_USER"),
            recipient_list=[email],
            fail_silently=False,
        )
        return redirect('users:email_confirmation_sent')


class EmailConfirmationSentView(TemplateView):
    template_name = 'email_confirm/email_confirmation_sent.html'


class ConfirmEmailView(View):
    """Представление для уникальной ссылки, отправленной пользователю на email. Активация профиля."""

    def get(self, request, uemailb64, token):
        uemail = urlsafe_base64_decode(uemailb64)
        user = CustomUser.objects.get(email=force_str(uemail))
        if default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            login(request, user)
            return render(request, "email_confirm/email_confirmation_done.html")


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
        pk = kwargs.get("pk")
        context["object"] = CustomUser.objects.get(pk=pk)
        return context
