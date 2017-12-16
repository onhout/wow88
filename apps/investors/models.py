from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Info(models.Model):
    BROKER_CHOICE = [
        ('amp', 'AMP'),
        ('rithmic', 'Rithmic'),
        ('eminis', 'Eminis Trader'),
        ('optimis', 'Optimus'),
        ('stagefive', 'Stage Five'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='investors_info')
    chosen_broker = models.CharField(max_length=25, choices=BROKER_CHOICE)
    invest_amount = models.IntegerField(blank=True, null=True)
    stripe_customer_id = models.CharField(max_length=50, blank=True, null=True)  # this id came from STRIPE
    stripe_customer_email = models.CharField(max_length=50, blank=True, null=True)  # this email came from STRIPE
    signup_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Contract(models.Model):
    CONTRACT_CHOICE = [
        ('ZB', '30 Year Bond'),
        ('ZF', '5 Year Note'),
        ('ZN', '10 Year Note'),
        ('6B', 'British Pound'),
        ('6E', 'Euro'),
        ('6J', 'Japanese Yen'),
        ('ZC', 'Corn'),
        ('ZL', 'Soybean Oil'),
        ('ZM', 'Soymeal'),
        ('ZS', 'Soybeans'),
        ('ZW', 'Wheat'),
        ('CL', 'Crude Oil'),
        ('NG', 'Natural Gas'),
        ('ES', 'S&P 500'),
        ('NQ', 'Nasdaq 100'),
        ('TF', 'Russell 2000'),
        ('YM', 'Dow 500'),
        ('GC', 'Gold'),
        ('HG', 'Copper'),
        ('SI', 'Silver'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscribed_contract')
    contract = models.CharField(max_length=25, choices=CONTRACT_CHOICE, blank=True, null=True)
    subscription_plan = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
