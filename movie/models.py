"""
This module defines the Movie model.

This model represents information about a movie including its title, genre,
release year, description, image, and trailer link. It also includes a method
to crop the associated image to a square shape.

Classes:
- Movie: Represents information about a movie.
"""

from io import BytesIO
from django.db import models
from django.core.files.base import ContentFile
from PIL import Image

class Tag(models.Model):
    """
    Tag Model represents tags associated with movies.
    """

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Movie(models.Model):
    """
    Movie Model represents information about a movie.

    Attributes:
    - title: The title of the movie.
    - genre: The genre of the movie.
    - release_year: The year the movie was released.
    - description: Description or summary of the movie.
    - directors: The directors of the movie.
    - country: The country of the movie production.
    - duration: Duration of the movie in minutes.
    - image: ImageField storing the movie's image.
    - trailer_link: URLField storing the link to the movie's trailer.
    - subscription_required: Indicates if the movie is part of a subscription plan.
    - created_at: Time the movie was posted.
    - tags: Many-to-many relationship with Tag model.
    """

    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    release_year = models.IntegerField()
    description = models.TextField()
    directors = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    duration = models.IntegerField(null=True, blank=True, verbose_name='Duration in minutes')
    image = models.ImageField(upload_to='movie_images/', blank=True, null=True)
    trailer_link = models.URLField(blank=True, null=True)
    subscription_required = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)
    
    def __str__(self):
        """
        Returns the title of the movie when it's converted to a string.
        """
        return f"{self.title}"

    def save(self, *args, **kwargs):
        if self.image:
            img = Image.open(self.image)
            output = BytesIO()

            # Define the aspect ratio (2:3)
            target_ratio = 2 / 3
            width, height = img.size
            current_ratio = width / height

            if current_ratio > target_ratio:
                # Calculate new height to maintain aspect ratio (2:3)
                new_height = int(width / target_ratio)
                top = (height - new_height) / 2
                bottom = (height + new_height) / 2
                img = img.crop((0, top, width, bottom))
            elif current_ratio < target_ratio:
                # Calculate new width to maintain aspect ratio (2:3)
                new_width = int(height * target_ratio)
                left = (width - new_width) / 2
                right = (width + new_width) / 2
                img = img.crop((left, 0, right, height))

            # Resize image to a reasonable size if needed
            max_size = (800, 1200)  # Adjust as necessary
            img.thumbnail(max_size)

            # Save the resized image to the BytesIO object
            img.save(output, format='JPEG', quality=75)
            output.seek(0)

            # Set the image content to the associated ImageField
            self.image.file = ContentFile(output.getvalue())

        super().save(*args, **kwargs)
