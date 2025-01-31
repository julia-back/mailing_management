from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Recipient, Message, Mailing
from django.urls import reverse_lazy
from .forms import RecipientForm, MessageForm, MailingForm


class HomeView(TemplateView):
    template_name = "mailing/home.html"


class RecipientListView(ListView):
    model = Recipient


class RecipientDetailView(DetailView):
    model = Recipient


class RecipientCreateView(CreateView):
    model = Recipient
    success_url = reverse_lazy("mailing:recipient_list")
    form_class = RecipientForm


class RecipientUpdateView(UpdateView):
    model = Recipient
    success_url = reverse_lazy("mailing:recipient_list")
    form_class = RecipientForm


class RecipientDeleteView(DeleteView):
    model = Recipient
    success_url = reverse_lazy("mailing:recipient_list")
    template_name = "mailing/confirm_delete.html"


class MessageListView(ListView):
    model = Message


class MessageDetailView(DetailView):
    model = Message


class MessageCreateView(CreateView):
    model = Message
    success_url = reverse_lazy("mailing:message_list")
    form_class = MessageForm


class MessageUpdateView(UpdateView):
    model = Message
    success_url = reverse_lazy("mailing:message_list")
    form_class = MessageForm


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy("mailing:message_list")
    template_name = "mailing/confirm_delete.html"


class MailingListView(ListView):
    model = Mailing


class MailingDetailView(DetailView):
    model = Mailing


class MailingCreateView(CreateView):
    model = Mailing
    success_url = reverse_lazy("mailing:mailing_list")
    form_class = MailingForm


class MailingUpdateView(UpdateView):
    model = Mailing
    success_url = reverse_lazy("mailing:mailing_list")
    form_class = MailingForm


class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy("mailing:mailing_list")
    template_name = "mailing/confirm_delete.html"
