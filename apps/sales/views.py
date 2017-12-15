from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from apps.user.decorators import user_is_salesperson, user_referral_code_is_empty


# Create your views here.


@login_required
@user_is_salesperson
def salesperson_index(request):
    return render(request, 'salesperson_dashboard.html', {
    })


@login_required
@user_referral_code_is_empty
def salesperson_signup(request):
    return render(request, 'salesperson_dashboard.html', {
    })
