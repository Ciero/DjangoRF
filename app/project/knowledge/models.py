from django.conf import settings
from django.db import models


class Knowledge(models.Model):
    CATEGORIES = [
        ('consulting', 'Consulting'),
        ('banking', 'Banking'),
        ('catering', 'Catering'),
        ('chemical', 'Chemical'),
        ('construction', 'Construction'),
        ('electronics', 'Electronics'),
        ('finance', 'Finance'),
        ('graphic art ', 'Graphic Art '),
        ('information', 'Information'),
        ('manufacturing', 'Manufacturing'),
        ('care', 'Care'),
        ('marketing', 'Marketing'),
        ('social', 'Social'),
        ('logistic', 'Logistics'),
        ('sales', 'Sales'),
        ('sport', 'Sport'),
        ('transport', 'Transport'),
    ]
    user = models.ForeignKey(
        verbose_name='user',
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='knowledge',
    )
    title = models.CharField(
        verbose_name='title',
        max_length=100,
    )
    description = models.TextField(
        verbose_name='description',
        max_length=250,
    )
    category = models.CharField(
        verbose_name='category',
        max_length=100,
        choices=CATEGORIES,
    )
    image = models.ImageField(
        verbose_name='picture of your knowledge',
        upload_to='knowledge/',
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ['-title']

    def __str__(self):
        return self.title
