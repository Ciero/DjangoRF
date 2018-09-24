# Generated by Django 2.0.7 on 2018-09-07 07:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import project.api.helpers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('knowledge', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=20, null=True, verbose_name='phone')),
                ('country', models.CharField(blank=True, max_length=100, null=True, verbose_name='country')),
                ('city', models.CharField(blank=True, max_length=100, null=True, verbose_name='city')),
                ('website', models.CharField(blank=True, max_length=100, null=True, verbose_name='website')),
                ('joined_date', models.DateTimeField(null=True, verbose_name='joined_date')),
                ('email', models.EmailField(max_length=200, verbose_name='email')),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='user_profile/', verbose_name='profile_picture')),
                ('code', models.CharField(default=project.api.helpers.code_generator, help_text='random code used for registration and for password reset', max_length=15, verbose_name='code')),
                ('knowledge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='knowledge.Knowledge', verbose_name='knowledge')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'User profile',
            },
        ),
    ]