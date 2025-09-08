from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class AppUser(AbstractUser):
    """Model representing a user in the application.

    Args:
        AbstractUser (class): Django's built-in abstract user model.
    """
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
            db_table = "app_user"


class UserAvatar(models.Model):
    """Model representing a user's avatar image.

    Args:
        models.Model (class): Base class for all Django models.
    """
    user = models.OneToOneField(AppUser, on_delete=models.CASCADE, related_name='avatar')
    image = models.ImageField(upload_to='avatars/') # Requires Pillow library

    def __str__(self):
        return f"Avatar for {self.user.username}"


class UserBanStatus(models.Model):
    """Model representing the ban status of a user.

    Args:
        models (class): Base class for all Django models.
    """
    user = models.OneToOneField(AppUser, on_delete=models.CASCADE, related_name='ban_status')
    is_banned = models.BooleanField(default=False)
    banned_date = models.DateTimeField(null=True, blank=True)
    ban_reason = models.CharField(max_length=120, blank=True)
    

class UserOnlineStatus(models.Model):
    """Model representing the online status of a user.

    Args:
        models (class): Base class for all Django models.
    """
    user = models.OneToOneField(AppUser, on_delete=models.CASCADE, related_name='online_status')
    status = models.CharField(max_length=10, default='Offline')
    last_seen = models.DateTimeField(auto_now=True)


class UserGamification(models.Model):
    """Model representing gamification attributes for a user.

    Args:
        models (class): Base class for all Django models.
    """
    user = models.OneToOneField(AppUser, on_delete=models.CASCADE, related_name='gamification')
    xp_points = models.IntegerField(default=0)
    level = models.IntegerField(default=1)
    rank = models.CharField(max_length=50, default='Novice')


class UserSolvedQuests(models.Model):
    """Model representing the number of solved quests by a user in different programming languages.

    Args:
        models (class): Base class for all Django models.
    """
    user = models.OneToOneField(AppUser, on_delete=models.CASCADE, related_name='solved_quests')
    total_solved = models.IntegerField(default=0)
    python = models.IntegerField(default=0)
    java = models.IntegerField(default=0)
    javascript = models.IntegerField(default=0)
    csharp = models.IntegerField(default=0)
    

class UserSubmittedQuests(models.Model):
    """Model representing the number of quests submitted by a user and their statuses.

    Args:
        models (class): Base class for all Django models.
    """
    user = models.OneToOneField(AppUser, on_delete=models.CASCADE, related_name='submitted_quests')
    total_submitted = models.IntegerField(default=0)
    approved = models.IntegerField(default=0)
    rejected = models.IntegerField(default=0)
    pending = models.IntegerField(default=0)