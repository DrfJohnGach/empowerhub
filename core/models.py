from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=50, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    goals = models.TextField(blank=True, null=True)
    progress = models.JSONField(default=dict)  # E.g., {"goal1": "completed", "goal2": "in progress"}
    privacy_settings = models.JSONField(default=dict)  # E.g., {"show_bio": True, "show_goals": False}
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nickname or self.user.username


class Group(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=100, blank=True, null=True)  # E.g., "Mental Health"
    group_icon = models.ImageField(upload_to='group_icons/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    admin = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='owned_groups')

    def __str__(self):
        return self.name


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()
    attachment = models.FileField(upload_to='post_attachments/', blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=[('active', 'Active'), ('hidden', 'Hidden'), ('deleted', 'Deleted')],
        default='active'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:50]
