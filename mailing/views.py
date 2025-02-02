from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView, View
from .models import Recipient, Message, Mailing, SendingAttempt
from django.urls import reverse_lazy
from .forms import RecipientForm, MessageForm, MailingForm, MailingModeratorForm
from .services import start_send_mailing


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "mailing/home.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context["success_attempt"] = SendingAttempt.objects.filter(status="success", owner=request.user).count()
        context["fail_attempt"] = SendingAttempt.objects.filter(status="fail", owner=request.user).count()
        context["all_attempt"] = SendingAttempt.objects.filter(owner=request.user).count()

        context["all_mailing"] = Mailing.objects.filter(owner=request.user).count()
        context["processing_mailing"] = Mailing.objects.filter(status="processing", owner=request.user).count()
        context["all_recipient"] = Recipient.objects.values("email").filter(owner=request.user).distinct().count()
        return self.render_to_response(context)


class SendingAttemptListView(LoginRequiredMixin, ListView):
    model = SendingAttempt

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.has_perm("view_sending_attempt"):
            return queryset
        queryset = queryset.filter(owner=self.request.user)
        return queryset


class RecipientListView(LoginRequiredMixin, ListView):
    model = Recipient

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.has_perm("view_recipient"):
            return queryset
        queryset = queryset.filter(owner=self.request.user)
        return queryset


class RecipientDetailView(LoginRequiredMixin, DetailView):
    model = Recipient


class RecipientCreateView(LoginRequiredMixin, CreateView):
    model = Recipient
    success_url = reverse_lazy("mailing:recipient_list")
    form_class = RecipientForm

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class RecipientUpdateView(LoginRequiredMixin, UpdateView):
    model = Recipient
    success_url = reverse_lazy("mailing:recipient_list")
    form_class = RecipientForm


class RecipientDeleteView(LoginRequiredMixin, DeleteView):
    model = Recipient
    success_url = reverse_lazy("mailing:recipient_list")
    template_name = "mailing/confirm_delete.html"


class MessageListView(LoginRequiredMixin, ListView):
    model = Message

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.has_perm("view_message"):
            return queryset
        queryset = queryset.filter(owner=self.request.user)
        return queryset


class MessageDetailView(LoginRequiredMixin, DetailView):
    model = Message


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    success_url = reverse_lazy("mailing:message_list")
    form_class = MessageForm

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    model = Message
    success_url = reverse_lazy("mailing:message_list")
    form_class = MessageForm


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = Message
    success_url = reverse_lazy("mailing:message_list")
    template_name = "mailing/confirm_delete.html"


class MailingListView(LoginRequiredMixin, ListView):
    model = Mailing

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.has_perm("view_mailing"):
            return queryset
        else:
            queryset = queryset.filter(owner=self.request.user)
            return queryset


class MailingDetailView(LoginRequiredMixin, DetailView):
    model = Mailing


class MailingCreateView(LoginRequiredMixin, CreateView):
    model = Mailing
    success_url = reverse_lazy("mailing:mailing_list")
    form_class = MailingForm

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class MailingUpdateView(LoginRequiredMixin, UpdateView):
    model = Mailing
    success_url = reverse_lazy("mailing:mailing_list")
    form_class = MailingForm

    def get_form_class(self):
        if self.request.user == self.object.owner:
            return MailingForm
        elif self.request.user.has_perm("can_stop_mailing"):
            return MailingModeratorForm


class MailingDeleteView(LoginRequiredMixin, DeleteView):
    model = Mailing
    success_url = reverse_lazy("mailing:mailing_list")
    template_name = "mailing/confirm_delete.html"


class MailingStartView(LoginRequiredMixin, View):

    def get(self, request, pk):
        return render(request, "mailing/mailing_start.html")

    def post(self, request, pk):
        start_send_mailing(pk=pk)
        return redirect("mailing:mailing_list")
