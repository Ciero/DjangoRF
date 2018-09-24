from django.contrib.auth import get_user_model
from rest_framework import serializers

from project.user_profile.models import UserProfile

User = get_user_model()


class UpdateUserProfileSerializer(serializers.ModelSerializer):
    handle = serializers.CharField()

    def get_handle(self, userprofile):
        return userprofile.user.handle

    class Meta:
        model = UserProfile
        fields = ['handle', 'website', 'location', 'email', 'bio', 'profile_pic', 'joined_date']
        read_only_fields = ['handle']

    def update(self, instance, validated_data):
        instance.handle = validated_data.get('handle', instance.handle)
        instance.website = validated_data.get('website', instance.website)
        instance.location = validated_data.get('location', instance.location)
        instance.email = validated_data.get('email', instance.email)
        instance.bio = validated_data.get('bio', instance.bio)
        instance.save()
        return instance



class UserSerializer(serializers.ModelSerializer):
    handle = serializers.SerializerMethodField()
    website = serializers.SerializerMethodField()
    location = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()
    bio = serializers.SerializerMethodField()
    profile_pic = serializers.SerializerMethodField()
    joined_date = serializers.SerializerMethodField()

    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'handle', 'website', 'location', 'email', 'bio' , 'profile_pic','joined_date']
        read_only_fields = fields

    def get_handle(self, user):
        return user.user_profile.handle
    
    def get_website(self, user):
        return user.user_profile.website

    def get_location(self, user):
        return user.user_profile.location

    def get_email(self, user):
        return user.user_profile.email
    
    def get_bio(self, user):
        return user.user_profile.bio

    def get_profile_pic(self, user):
        if user.user_profile.profile_pic:
            return user.user_profile.profile_pic.url
        return "Nope"

    def get_joined_date(self, user):
        return user.user_profile.joined_date
