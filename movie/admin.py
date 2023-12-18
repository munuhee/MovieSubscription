"""
This module contains the configuration for the Django admin panel for the Movie model.
"""

from django.contrib import admin
from .models import Movie
from PIL import Image

class MovieAdmin(admin.ModelAdmin):
    """
    MovieAdmin class defines the configuration for the Movie model in the Django admin panel.

    Attributes:
    - list_display: Specifies the fields to be displayed in the list view of Movie objects.
    - list_filter: Specifies the fields used for filtering Movie objects in the admin panel.
    - search_fields: Specifies the fields used for searching Movie objects in the admin panel.
    """

    list_display = ('title', 'genre', 'release_year', 'has_image')
    list_filter = ('genre', 'release_year')
    search_fields = ('title', 'genre', 'description')

    def has_image(self, obj):
        """
        Custom method to check if the Movie object has an associated image.

        Args:
        - obj: The Movie object.

        Returns:
        - Boolean: True if the Movie object has an image, otherwise False.
        """
        return bool(obj.image)

    has_image.boolean = True
    has_image.short_description = 'Has Image'

admin.site.register(Movie, MovieAdmin)
