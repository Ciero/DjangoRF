from django.contrib.auth import get_user_model
from django.core.mail import EmailMessage
from rest_framework import serializers

from project.user_profile.models import UserProfile

User = get_user_model()


class RegistrationSerializer(serializers.Serializer):
    email = serializers.EmailField(
        label='Registration e-mail address'
    )

    def validate_email(self, email):
        try:
            User.objects.get(email=email)
            raise serializers.ValidationError('User with this email already exists!')
        except User.DoesNotExist:
            return email

    @staticmethod
    def send_registration_email(email, code):
        message = EmailMessage(
            subject='Suprset Registration',
            body=f"Welcome! Thanks for registering. Please enter this code {code} on the verify page.",
            to=[email],
        )
        message.send()

    def save(self, validated_data):
        email = validated_data.get('email')
        new_user = User.objects.create_user(
            username=email,
            email=email,
            is_active=False
        )
        new_profile = UserProfile.objects.create(
            user=new_user
        )
        self.send_registration_email(
            email=email,
            code=new_profile.registration_code,
        )
        return new_user


class RegistrationValidationSerializer(RegistrationSerializer):
    code = serializers.CharField(
        label='code',
        write_only=True
    )
    password = serializers.CharField(
        label='password',
        write_only=True
    )
    password_repeat = serializers.CharField(
        label='password_repeat',
        write_only=True
    )
    username = serializers.CharField(
        label='username',
    )
    email = serializers.EmailField(
        label='email'
    )

    def validate_email(self, email):
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError('This email is not valid!')


    def validate(self, data):
        user = data.get('email')
        if data.get('password') != data.get('password_repeat'):
            raise serializers.ValidationError({
                'password_repeat': 'Passwords do not match!'
            })

        if data.get('code') != user.user_profile.registration_code or user.is_active:
            raise serializers.ValidationError({
                'code': 'Wrong code or already validated!'
            })
        return data

    def save(self, validated_data):
        user = validated_data.get('email')
        user.email = validated_data.get('email').email
        user.is_active = True
        user.set_password(validated_data.get('password'))
        user.save()
        return user