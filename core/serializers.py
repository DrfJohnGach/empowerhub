from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile, Group, Post


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # Nested User data (read-only)

    class Meta:
        model = Profile
        fields = ['id', 'user', 'nickname', 'bio', 'goals', 'progress', 'profile_picture', 'privacy_settings']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name', 'description', 'category', 'group_icon', 'created_at']


class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # Nested User data (read-only)
    group = serializers.StringRelatedField()  # Display group name instead of ID

    class Meta:
        model = Post
        fields = ['id', 'user', 'group', 'content', 'attachment', 'status', 'created_at']
