from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Email(models.Model):
    to = models.EmailField(verbose_name='To')
    subject = models.CharField(verbose_name='Subject', max_length=200)
    content = models.TextField(verbose_name='Content')
    is_sent = models.BooleanField(verbose_name='is_sent', default=False)


class Codes(models.Model):
    user = models.OneToOneField(to=User, verbose_name='User', related_name='validation_code', null=True, blank=True, on_delete=models.CASCADE)
    code = models.CharField(max_length=6, verbose_name='Validation Code')
    email = models.EmailField(verbose_name='Email')
