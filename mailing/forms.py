from django.forms import ModelForm
from .models import Recipient, Message, Mailing


class RecipientForm(ModelForm):
    class Meta:
        model = Recipient
        fields = "__all__"


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = "__all__"


class MailingForm(ModelForm):
    class Meta:
        model = Mailing
        fields = ["name", "message", "recipient"]
