from datetime import datetime
from django.utils import timezone
from datetime import timedelta
import paypalrestsdk
from paypalrestsdk import Payment
from django.urls import reverse
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Subscription, UserSubscription
from django.contrib.auth.decorators import login_required

def subscriptions_list(request):
    subscriptions = Subscription.objects.all()
    context = {
        'subscriptions': subscriptions
    }
    return render(request, 'subscription/subscriptions_list.html', context)

@login_required
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

@login_required
def checkout(request):
    if request.method == 'POST':
        subscription_id = request.POST.get('subscription_id')
        selected_duration = request.POST.get('selected_duration')
        
        # Retrieve the selected price based on the selected duration
        if selected_duration == 'monthly':
            selected_price = request.POST.get('monthly_price')
            duration_in_days = 31
        elif selected_duration == 'semi_annual':
            selected_price = request.POST.get('semi_annual_price')
            duration_in_days = 183
        elif selected_duration == 'annual':
            selected_price = request.POST.get('annual_price')
            duration_in_days = 366
        else:
            # Handle invalid duration selection
            return HttpResponse("Invalid duration selection")

        # Calculate start and end dates
        start_date = datetime.now().date()
        end_date = start_date + timedelta(days=duration_in_days)
        
        # Assuming the user is already authenticated
        user = request.user
        
        # Create UserSubscription object with calculated dates
        user_subscription = UserSubscription.objects.create(
            user=user,
            subscription_id=subscription_id,  # Assuming the subscription ID is used
            start_date=start_date,
            end_date=end_date
        )

        # Further processing for checkout (PayPal or other payment gateway integration)
        return render(request, 'subscription/checkout.html', {
            'selected_price': selected_price,
            'subscription_id': subscription_id,
            'csrf_token': request.COOKIES['csrftoken'],
            'paypal_client_id': settings.PAYPAL_CLIENT_ID,
            'paypal_mode': settings.PAYPAL_MODE
        })
    else:
        # Handle GET request or invalid form submissions
        # Redirect or render appropriate response
        return render(request, 'subscription/checkout.html')
