from django.conf import settings
from django.db import models


class Comment(models.Model):
    comment_sender = models.ForeignKey(
        verbose_name='comment_sender',
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    comment_receiver = models.ForeignKey(
        verbose_name='comment_receiver',
        to='user_profile.UserProfile',
        on_delete=models.CASCADE,
        related_name='commented',
    )
    content = models.CharField(
        verbose_name='content',
        max_length=5000,
    )
    date_created = models.DateTimeField(
        verbose_name='date_created',
        null=True,
        auto_now_add=True,
    )

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.content
