import smtplib

from .models import Mailing, SendingAttempt
from django.core.mail import send_mail
import os
from dotenv import load_dotenv


load_dotenv()


def start_send_mailing(pk):
    mailing = Mailing.objects.get(pk=pk)
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

    mailing.status = mailing.STATUS_MAILING_CHOICES.get("processing")
    mailing.save()
