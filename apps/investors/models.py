from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Info(models.Model):
    BROKER_CHOICE = [
        ('pricefutures', 'Price Futures (preferred)'),
        ('amp', 'AMP'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='investors_info')
    chosen_broker = models.CharField(max_length=25, choices=BROKER_CHOICE)
    invest_amount = models.IntegerField(blank=True, null=True)
    contracts_traded = models.IntegerField(blank=True, null=True)
    stripe_customer_id = models.CharField(max_length=50, blank=True, null=True)  # this id came from STRIPE
    stripe_customer_email = models.CharField(max_length=50, blank=True, null=True)  # this email came from STRIPE
    signup_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)