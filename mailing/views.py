from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView, View
from .models import Recipient, Message, Mailing, SendingAttempt
from django.urls import reverse_lazy
from .forms import RecipientForm, MessageForm, MailingForm
from .services import start_send_mailing


class HomeView(TemplateView):
    template_name = "mailing/home.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context["success_attempt"] = SendingAttempt.objects.filter(status="success").count()
        context["fail_attempt"] = SendingAttempt.objects.filter(status="fail").count()
        context["all_attempt"] = SendingAttempt.objects.count()

        context["all_mailing"] = Mailing.objects.count()
        context["processing_mailing"] = Mailing.objects.filter(status="processing").count()
        context["all_recipient"] = Recipient.objects.values("email").distinct().count()

        return self.render_to_response(context)


class SendingAttemptListView(ListView):
    model = SendingAttempt


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


class MailingStartView(View):

    def get(self, request, pk):
        return render(request, "mailing/mailing_start.html")

    def post(self, request, pk):
        start_send_mailing(pk=pk)
        return redirect("mailing:mailing_list")
