from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Info(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='sales_info')
    contract_agreement = models.BooleanField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Customers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='salesperson')
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer')
    signup_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
