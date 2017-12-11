from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class Profile(models.Model):
    USER_TYPE = [
        ('investor', 'Investor'),
        ('sales', 'Sales'),
        ('both', 'Both'),
    ]
    BROKER_CHOICE = [
        ('amp', 'AMP'),
        ('rithmic', 'Rithmic'),
        ('eminis', 'Eminis Trader'),
        ('optimis', 'Optimus'),
        ('stagefive', 'Stage Five'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    type = models.CharField(max_length=15, choices=USER_TYPE, default="investor")
    broker = models.CharField(max_length=100, choices=BROKER_CHOICE, blank=True, null=True)
    referral_code = models.CharField(max_length=20)
    trading_experience = models.CharField(max_length=10, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)


class Address(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='address')
    address = models.CharField(max_length=255)
    address2 = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=50)
    updated_at = models.DateTimeField(auto_now=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        Address.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    instance.address.save()
