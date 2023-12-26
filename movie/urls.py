from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'movies'

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('popular/', views.popular_movies, name='popular_movies_list'),
    path('new-movies/', views.new_movies, name='new_movies_list'),
    path('tv-series/', views.tv_series, name='tv_series_list'),
    path('create/', views.movie_create, name='movie_create'),
    path('<slug:slug>/', views.movie_detail, name='movie_detail'),
    path('<slug:slug>/update/', views.movie_update, name='movie_update'),
    path('<slug:slug>/delete/', views.movie_delete, name='movie_delete'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
