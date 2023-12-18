"""
Application configuration for user_profile app.
"""

from django.apps import AppConfig

class UserProfileConfig(AppConfig):
    """Configuration for the user_profile app."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_profile'

    def ready(self):
        """Import signal handlers when the app is ready."""
        import user_profile.signals
