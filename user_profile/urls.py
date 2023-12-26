from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'account'

urlpatterns = [
    path('profile/', views.user_profile_detail, name='user_profile_detail'),
    path('profile/edit/', views.edit_user_profile, name='edit_user_profile'),
    path('watchlist/add/<slug:movie_id>/', views.add_to_watchlist, name='add_to_watchlist'),
    path('watchlist/remove/<slug:movie_id>/', views.remove_from_watchlist, name='remove_from_watchlist'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='user_profile/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
