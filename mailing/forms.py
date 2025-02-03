from django.forms import ModelForm
from .models import Recipient, Message, Mailing
from .services import StyleFormMixin


class RecipientForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Recipient
        exclude = ["owner"]


class MessageForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Message
        exclude = ["owner"]


class MailingForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Mailing
        fields = ["name", "message", "recipient"]


class MailingModeratorForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Mailing
        fields = ["status"]
