import time
from django.conf import settings
from django.core.mail import send_mail
from django.core.management.base import BaseCommand

from project.email.models import Email


class Command(BaseCommand):
    help = 'Send Mails'

    def handle(self, *args, **options):
        while True:
            time.sleep(10)
            emails = Email.objects.filter(is_sent=False)
            for email in emails:
                send_mail(
                    email.subject,
                    email.content,
                    settings.DEFAULT_FROM_EMAIL,
                    [email.to],
                    fail_silently=False,
                )
                email.is_sent = True
                email.save()
