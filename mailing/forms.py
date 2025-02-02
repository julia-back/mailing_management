from django.forms import ModelForm
from .models import Recipient, Message, Mailing


class RecipientForm(ModelForm):
    class Meta:
        model = Recipient
        exclude = ["owner"]


class MessageForm(ModelForm):
    class Meta:
        model = Message
        exclude = ["owner"]


class MailingForm(ModelForm):
    class Meta:
        model = Mailing
        fields = ["name", "message", "recipient"]
