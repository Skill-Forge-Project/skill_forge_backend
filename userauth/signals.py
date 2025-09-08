from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import AppUser, UserAvatar
from django.core.files import File
import os

@receiver(post_save, sender=AppUser)
def create_default_avatar(sender, instance, created, **kwargs):
    if created:
        default_path = os.path.join('media', 'avatars', 'default_avatar.png')
        with open(default_path, 'rb') as f:
            avatar = UserAvatar(user=instance)
            avatar.image.save('default.png', File(f), save=True)