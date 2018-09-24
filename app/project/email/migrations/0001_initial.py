# Generated by Django 2.0.7 on 2018-09-12 09:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Codes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=6, verbose_name='Validation Code')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='validation_code', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to', models.EmailField(max_length=254, verbose_name='To')),
                ('subject', models.CharField(max_length=200, verbose_name='Subject')),
                ('content', models.TextField(verbose_name='Content')),
                ('is_sent', models.BooleanField(default=False, verbose_name='is_sent')),
            ],
        ),
    ]
