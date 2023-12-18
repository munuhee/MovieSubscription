from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """
    Admin configuration for the UserProfile model.
    """
    list_display = ('user', 'display_watchlist')
    def display_watchlist(self, obj):
        return ", ".join([movie.title for movie in obj.watchlist.all()])

    display_watchlist.short_description = 'Watchlist'

    search_fields = ('user__username',)
