from datetime import datetime
from django.utils import timezone
from datetime import timedelta
import paypalrestsdk
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Subscription, UserSubscription
from django.contrib.auth.decorators import login_required

paypalrestsdk.configure({
    "mode": settings.PAYPAL_MODE,
    "client_id": settings.PAYPAL_CLIENT_ID,
    "client_secret": settings.PAYPAL_CLIENT_SECRET
})

def subscriptions_list(request):
    subscriptions = Subscription.objects.all()
    context = {
        'subscriptions': subscriptions
    }
    return render(request, 'subscription/subscriptions_list.html', context)

def subscription_detail(request, pk):
    """Renders details of a specific subscription based on its primary key."""
    subscription = get_object_or_404(Subscription, pk=pk)

    monthly_price = round(subscription.price, 2)
    semi_annual_price = round(monthly_price * 6 * 0.8, 2)  # 20% discount for 6 months
    annual_price = round(monthly_price * 12 * 0.65, 2)  # 35% discount for 12 months
    context = {
        'subscription': subscription,
        'monthly_price': monthly_price,
        'semi_annual_price': semi_annual_price,
        'annual_price': annual_price,
    }
    return render(request, 'subscription/subscription_detail.html', context)

def checkout(request):
    if request.method == 'POST':
        subscription_id = request.POST.get('subscription_id')
        duration = request.POST.get('duration')
        price = request.POST.get('price')
        
        # Fetch subscription details
        subscription = Subscription.objects.get(pk=subscription_id)
        
        # Calculate end date based on duration chosen
        if duration == 'monthly':
            duration_in_days = 30
        elif duration == 'semi_annual':
            duration_in_days = 30 * 6
        elif duration == 'annual':
            duration_in_days = 365  # Adjust for leap years if needed
        
        # Calculate start and end dates
        start_date = datetime.now().date()
        end_date = start_date + timedelta(days=duration_in_days)
        
        # Assuming the user is already authenticated
        user = request.user
        
        # Create UserSubscription object with calculated dates
        user_subscription = UserSubscription.objects.create(
            user=user,
            subscription=subscription,
            start_date=start_date,
            end_date=end_date
        )
        
        # Additional logic like payment processing, etc., can be added here
        
        return HttpResponse(f'Subscription successful! End date: {end_date}')
    
    return HttpResponse('Invalid request')