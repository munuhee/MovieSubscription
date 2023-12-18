"""
Module: review.py
Description: Contains the Review model for user reviews related to movies.
"""

from django.db import models
from django.contrib.auth.models import User
from movie.models import Movie

class Review(models.Model):
    """
    Represents a review related to a movie in the application.

    Attributes:
    - user (ForeignKey[User]): Foreign key relationship with the User model from Django's auth system.
    - movie (ForeignKey[Movie]): Foreign key relationship with the Movie model.
    - rating (float): The rating given for the movie.
    - comment (str): The comment or review content.
    # Add other review-related fields
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.FloatField()
    comment = models.TextField()

    def __str__(self):
        return f"{self.user.username} - {self.movie.title}"
