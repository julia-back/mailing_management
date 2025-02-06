import datetime
import os
import smtplib

from django.core.mail import send_mail
from django.db import models
from dotenv import load_dotenv

from .models import Mailing, SendingAttempt

load_dotenv()


def start_send_mailing(pk):
    mailing = Mailing.objects.get(pk=pk)
    if mailing.status != "completed":
        message_subject = mailing.message.message_subject
        message_body = mailing.message.message_body
        recipient_queryset = mailing.recipient.all()
        email_list = []
        for recipient in recipient_queryset:
            email_list.append(recipient.email)
        try:
            send_mail(subject=message_subject, message=message_body, recipient_list=email_list, fail_silently=False,
                      from_email=os.getenv("EMAIL_HOST_USER"))
        except smtplib.SMTPException as err:
            sending_attempt_fail = SendingAttempt(status="fail", mail_server_response=err, mailing=mailing)
            sending_attempt_fail.save()
        else:
            sending_attempt_success = SendingAttempt(status="success", mail_server_response=None, mailing=mailing)
            sending_attempt_success.save()
        mailing.status = "processing"
        mailing.start_send = datetime.datetime.now()
        mailing.save()


class StyleFormMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field, value in self.fields.items():
            if isinstance(value, models.BooleanField):
                value.widget.attrs.update({"class": "form-check"})
            else:
                value.widget.attrs.update({"class": "form-control"})
