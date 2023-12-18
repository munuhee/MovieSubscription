from django.contrib import admin
from .models import Subscription, UserSubscription, Benefit
from django.contrib import admin

@admin.register(Benefit)
class BenefitAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'duration_in_days', 'is_active')
    list_filter = ('is_active', )
    search_fields = ('name', 'description')
    ordering = ('name',)

@admin.register(UserSubscription)
class UserSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'subscription', 'start_date', 'end_date')
    list_filter = ('start_date', 'end_date')
    search_fields = ('user__username', 'subscription__name')
    ordering = ('user', 'start_date')
