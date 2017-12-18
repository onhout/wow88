from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from apps.user.decorators import user_is_investor, user_referral_code_is_empty
from apps.user.models import Profile
from . import forms as investors_forms
from .models import Info


# Create your views here.
@login_required
@user_is_investor
def investors_index(request):
    investor_info = Info.objects.get(user=request.user)
    return render(request, 'investors_dashboard.html', {
        'investor_info': investor_info
    })


@login_required
@user_referral_code_is_empty
def investors_signup(request):
    if not request.user.investors_info.chosen_broker:
        if request.method == 'POST':
            investor_info_form = investors_forms.ChooseBroker(request.POST, instance=request.user.investors_info)
            if investor_info_form.is_valid():
                investor = investor_info_form.save(commit=False)
                investor.user = request.user
                investor.save()
                return redirect('investors_verify')

        investor_info_form = investors_forms.ChooseBroker()
        return render(request, 'investors_signup.html', {
            'investorform': investor_info_form
        })
    else:
        return redirect('investors_verify')


@login_required
@user_referral_code_is_empty
def investor_verify(request):
    if request.user.investors_info.chosen_broker:
        if request.method == 'POST':
            investor_info_form = investors_forms.VerifyAmountInvested(request.POST,
                                                                      instance=request.user.investors_info)
            if investor_info_form.is_valid():
                user_profile = Profile.objects.get(user=request.user)
                user_profile.potential = 0
                user_profile.save()
                investor = investor_info_form.save(commit=False)
                investor.user = request.user
                investor.signup_date = datetime.now()
                investor.save()
                return redirect('investors_index')

        investor_info_form = investors_forms.VerifyAmountInvested(instance=request.user.investors_info)
        return render(request, 'investors_verify.html', {
            'investorform': investor_info_form
        })
    else:
        return redirect('investors_signup')
