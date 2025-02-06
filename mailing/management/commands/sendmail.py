from django.core.management.base import BaseCommand

from mailing.services import start_send_mailing


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("mailing_pk", type=int, help="Argument mailing pk/id")

    def handle(self, *args, **options):
        mailing_pk = options["mailing_pk"]
        start_send_mailing(pk=mailing_pk)
