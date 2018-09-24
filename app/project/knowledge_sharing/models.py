from django.conf import settings
from django.db import models


class KnowledgeSharing(models.Model):
        PENDING = 'pending'
        ACCEPTED = 'accepted'
        DECLINED = 'declined'
        STATUS_CHOICES = [
            (PENDING, 'Knowledge request pending'),
            (ACCEPTED, 'Knowledge request accepted'),
            (DECLINED, 'Knowledge request declined')
        ]

        sender = models.ForeignKey(
            verbose_name='sender',
            to=settings.AUTH_USER_MODEL,
            blank=True,
            related_name='knowledge_request',
            on_delete=models.CASCADE
        )
        receiver = models.ForeignKey(
            verbose_name='receiver',
            to=settings.AUTH_USER_MODEL,
            blank=True,
            related_name='knowledge_requested',
            on_delete=models.CASCADE
        )
        status = models.CharField(
            verbose_name='status',
            choices=STATUS_CHOICES,
            default=PENDING,
            max_length=10,
        )