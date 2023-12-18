from django.db import models
from django.contrib.auth.models import User

class Benefit(models.Model):
    """
    Benefit Model represents different benefits available for subscription plans.

    Attributes:
    - name: The name of the benefit.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Subscription(models.Model):
    """
    Subscription Model represents different subscription plans available.

    Attributes:
    - name: The name of the subscription plan.
    - price: The price of the subscription plan.
    - benefits: Many-to-Many relationship with Benefit model.
    - duration_in_days: Duration of the subscription plan in days.
    - is_active: Boolean field to indicate if the subscription is currently active.
    """
    name = models.CharField(max_length=100)
    price = models.FloatField()
    benefits = models.ManyToManyField(Benefit)
    duration_in_days = models.PositiveIntegerField(default=30)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} - ${self.price}"

class UserSubscription(models.Model):
    """
    UserSubscription Model links users to their chosen subscription plans.

    Attributes:
    - user: The user associated with the subscription.
    - subscription: The chosen subscription plan.
    - start_date: The start date of the subscription.
    - end_date: The end date of the subscription.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.subscription.name}"
