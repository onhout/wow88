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
        ('gc', 'GC'),
        ('ng', 'NG'),
        ('cl', 'CL'),
        ('si', 'SI'),
        ('hg', 'HG'),
        ('andmore', 'AND MORE')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscribed_contract')
    contract = models.CharField(max_length=25, choices=CONTRACT_CHOICE, blank=True, null=True)
    subscription_plan = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
