"""
Contains signal handlers for user profile operations.
"""

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile

@receiver(post_save, sender=User)
def create_profile(instance, created, **_):
    """Create a UserProfile when a User is created."""
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(instance, **_):
    """Save the UserProfile when a User is updated."""
    instance.userprofile.save()
