from django.urls import path
from . import views

app_name = 'subscription'

urlpatterns = [
    path('', views.subscriptions_list, name='subscriptions_list'),
    path('<int:pk>/', views.subscription_detail, name='subscription_detail'),
    path('checkout/', views.checkout, name='checkout'), 
]
