import random

from django.conf import settings
from django.db import models


def code_generator(length=6):
    numbers = '0123456789'
    return ''.join(random.choice(numbers) for i in range(length))


class UserProfile(models.Model):
    user = models.OneToOneField(
        verbose_name='user',
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='user_profile',
    )
    # knowledge = models.ForeignKey(
    #     verbose_name='knowledge',
    #     to='knowledge.Knowledge',
    #     on_delete=models.CASCADE,
    # )
    # comment = models.ForeignKey(
    #     verbose_name='comment',
    #     to='comment.Comment',
    #     on_delete=models.CASCADE,
    #     blank=True,
    # )
    handle = models.CharField(
        verbose_name='handle',
        null=True,
        blank=True,
        max_length=150,
    )
    website = models.CharField(
        verbose_name='website',
        max_length=100,
        blank=True,
        null=True,
    )
    location = models.CharField(
        verbose_name='location',
        null=True,
        blank=True,
        max_length=100,
    )
    email = models.EmailField(
        verbose_name='email',
        max_length=200,
        null=True,
        blank=True,
    )
    bio = models.TextField(
        verbose_name='bio',
        null=True,
        blank=True,
        max_length=200,
    )

    profile_pic = models.ImageField(
        verbose_name='profile_picture',
        null=True,
        blank=True,
        upload_to='user_profile/',
    )
    joined_date = models.DateTimeField(
        verbose_name='joined_date',
        null=True,
        blank=True,
    )
    registration_code = models.CharField(
        verbose_name='registration_code',
        max_length=15,
        default=code_generator,
    )

    def __str__(self):
        return self.user.username

    def generate_new_code(self):
        self.registration_code = code_generator()
        self.save()
        return self.registration_code

    class Meta:
        verbose_name = 'User profile'

    def __str__(self):
        return self.email
