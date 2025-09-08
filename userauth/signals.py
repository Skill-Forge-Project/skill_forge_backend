from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.files import File
from .models import (
    AppUser,
    UserAvatar,
    UserBanStatus,
    UserOnlineStatus,
    UserGamification,
    UserSolvedQuests,
    UserSubmittedQuests,
    UserSocialLinks
)
import os

@receiver(post_save, sender=AppUser)
def initialize_user_related_models(sender, instance, created, **kwargs):
    """
    Signal to initialize all related models for a newly registered AppUser.

    This includes:
    - Assigning a default avatar image
    - Creating ban status record (not banned by default)
    - Setting online status to 'Offline' by default. It will be updated upon user login.
    - Initializing gamification stats. These will be updated as the user earns points and badges.
    - Creating quest tracking records. They will be updated as the user interacts with quests.
    - Linking empty social media profiles. Users can update these later.

    Args:
        sender (Model): The AppUser model.
        instance (AppUser): The newly created user instance.
        created (bool): Whether this is a new user creation.
        **kwargs: Additional keyword arguments.
    """
    if not created:
        return

    # 1. Default Avatar
    try:
        default_path = os.path.join('media', 'avatars', 'default_avatar.png')
        with open(default_path, 'rb') as f:
            avatar = UserAvatar(user=instance)
            avatar.image.save('user_default_avatar.png', File(f), save=True)
    except Exception as e:
        raise RuntimeError(f"Failed to assign default avatar: {e}")

    # 2. Ban Status
    UserBanStatus.objects.create(user=instance)

    # 3. Online Status
    UserOnlineStatus.objects.create(user=instance, status='Offline')

    # 4. Gamification
    UserGamification.objects.create(user=instance)

    # 5. Solved Quests
    UserSolvedQuests.objects.create(user=instance)

    # 6. Submitted Quests
    UserSubmittedQuests.objects.create(user=instance)

    # 7. Social Links
    UserSocialLinks.objects.create(user=instance)