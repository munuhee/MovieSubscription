from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Review model.
    """
    list_display = ('user', 'movie', 'rating')
    search_fields = ('user__username', 'movie__title')
    list_filter = ('rating',)
