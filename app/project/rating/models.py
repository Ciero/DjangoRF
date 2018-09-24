from django.conf import settings
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Rating(models.Model):
    user = models.ForeignKey(
        verbose_name='user',
        to=settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name='sender',
        null=True
    )   
    receiver = models.ForeignKey(
        verbose_name='receiver',
        to=settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name='receiver',
        null=True,
    )
    knowledge = models.ForeignKey(
        verbose_name='knowledge ',
        to='knowledge.Knowledge',
        # when knowledge is deleted the rating also go away
        on_delete=models.CASCADE,
        blank=True,
    )
    date_created = models.DateTimeField(
        verbose_name='date_created',
        null=True,
        auto_now_add=True,
    )
    rating = models.IntegerField(
        verbose_name='rating',
        default=1,
        validators=[MaxValueValidator(5), MinValueValidator(1)],
    )
   
    class Meta:
        unique_together = ('user', 'receiver', 'knowledge')

