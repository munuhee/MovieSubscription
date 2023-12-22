"""
Contains view functions related to user profiles and watchlists.

This module includes various view functions for managing user profiles, 
such as displaying user profile details,editing user profiles, and managing 
watchlists by adding or removing movies.
"""

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse, Http404
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm, SignUpForm
from movie.models import Movie

@login_required
def user_profile_detail(request):
    """
    View function to display a user's profile details.

    Args:
    - request: HTTP request object

    Returns:
    - Rendered HTML template with user profile details
    """
    try:
        user_profile = get_object_or_404(UserProfile, user=request.user)
        context = {
            'user_profile': user_profile,
        }
        return render(request, 'user_profile/detail.html', context)
    except UserProfile.DoesNotExist:
        raise Http404("User profile does not exist")

@login_required
def edit_user_profile(request):
    """
    View function to edit a user's profile.

    Args:
    - request: HTTP request object

    Returns:
    - Rendered HTML template for editing user profile
    """
    try:
        user_profile = get_object_or_404(UserProfile, user=request.user)
        if request.method == 'POST':
            form = UserProfileForm(request.POST, instance=user_profile)
            if form.is_valid():
                form.save()
                # Redirect or show success message
        else:
            form = UserProfileForm(instance=user_profile)

        context = {
            'form': form,
        }
        return render(request, 'user_profile/edit.html', context)
    except UserProfile.DoesNotExist:
        raise Http404("User profile does not exist")

@login_required
def add_to_watchlist(request, movie_id):
    """
    View function to add a movie to the user's watchlist.

    Args:
    - request: HTTP request object
    - movie_id: ID of the movie to add to the watchlist

    Returns:
    - Redirect or success message upon adding the movie to the watchlist
    """
    try:
        user_profile = get_object_or_404(UserProfile, user=request.user)
        movie = get_object_or_404(Movie, pk=movie_id)
        user_profile.watchlist.add(movie)
        # Redirect or show success message
    except (UserProfile.DoesNotExist, Movie.DoesNotExist):
        raise Http404("User profile or movie does not exist")

@login_required
def remove_from_watchlist(request, movie_id):
    """
    View function to remove a movie from the user's watchlist.

    Args:
    - request: HTTP request object
    - movie_id: ID of the movie to remove from the watchlist

    Returns:
    - Redirect or success message upon removing the movie from the watchlist
    """
    try:
        user_profile = get_object_or_404(UserProfile, user=request.user)
        movie = get_object_or_404(Movie, pk=movie_id)
        user_profile.watchlist.remove(movie)
        # Redirect or show success message
    except (UserProfile.DoesNotExist, Movie.DoesNotExist):
        raise Http404("User profile or movie does not exist")

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'user_profile/signup.html', {'form': form})
