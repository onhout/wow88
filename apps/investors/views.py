from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from apps.user.decorators import user_is_investor, user_referral_code_is_empty
from . import forms as investors_forms


# Create your views here.
@login_required
@user_is_investor
def investors_index(request):
    return render(request, 'investors_dashboard.html', {
    })


@login_required
@user_referral_code_is_empty
def investors_signup(request):
    if request.method == 'POST':
        investor_info_form = investors_forms.ChooseBroker(request.POST, instance=request.user)
        if investor_info_form.is_valid():
            investor_info_form.save()

    investor_info_form = investors_forms.ChooseBroker(instance=request.user)
    return render(request, 'investors_signup.html', {
        'investorform': investor_info_form
    })
