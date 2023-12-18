
"""
This module contains views to perform CRUD operations on Movie model.

These views handle rendering a list of movies, displaying details of a specific movie,
creating new movies, updating existing movies, and deleting movies.

Functions:
- movie_list: Renders a list of movies.
- movie_detail: Renders details of a specific movie based on its primary key.
- movie_create: Handles the creation of a new movie.
- movie_update: Handles updating an existing movie.
- movie_delete: Handles the deletion of an existing movie.
"""
import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseBadRequest
from .forms import MovieForm
from review.forms import ReviewForm
from .models import Movie
from subscription.models import UserSubscription
from review.models import Review

def movie_list(request):
    """Renders a list of movies."""
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movie/movie_list.html', context)

def movie_detail(request, pk):
    """Renders details of a specific movie based on its primary key."""
    movie = get_object_or_404(Movie, pk=pk)
    reviews = Review.objects.filter(movie=movie)
    reviews_count = reviews.count()
    
    if movie.subscription_required:
        user_subscription = UserSubscription.objects.filter(user=request.user).first()
        if not user_subscription or user_subscription.end_date < datetime.date.today():
            return redirect('subscription:subscriptions_list')
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.user = request.user
            new_review.movie = movie
            new_review.save()
            return redirect('movies:movie_detail', pk=pk)
    else:
        form = ReviewForm()

    context = {
        'movie': movie,
        'reviews': reviews,
        'reviews_count': reviews_count,
        'form': form,
    }
    return render(request, 'movie/movie_detail.html', context)

def movie_create(request):
    """Handles the creation of a new movie."""
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
        else:
            return render(request, 'movie/movie_form.html', {'form': form})
    else:
        form = MovieForm()
    return render(request, 'movie/movie_form.html', {'form': form})

def movie_update(request, pk):
    """Handles updating an existing movie."""
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
        else:
            return render(request, 'movie/movie_form.html', {'form': form})
    else:
        form = MovieForm(instance=movie)
    return render(request, 'movie/movie_form.html', {'form': form})

def movie_delete(request, pk):
    """Handles the deletion of an existing movie."""
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        try:
            movie.delete()
            return redirect('movie_list')
        except Exception as e:
            return HttpResponseBadRequest("Error deleting movie.")
    return render(request, 'movie/movie_confirm_delete.html', {'movie': movie})
