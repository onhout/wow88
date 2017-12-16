from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

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
                investor = investor_info_form.save(commit=False)
                investor.user = request.user
                investor.save()
                return redirect('add_new_contract')

        investor_info_form = investors_forms.VerifyAmountInvested(instance=request.user.investors_info)
        return render(request, 'investors_verify.html', {
            'investorform': investor_info_form
        })
    else:
        return redirect('investors_signup')


@login_required
@user_referral_code_is_empty
def contract_form(request):
    if request.user.investors_info.chosen_broker and request.user.investors_info.invest_amount:
        contractform = investors_forms.CreateContractForm()
        return render(request, 'contract.html', {
            'contractform': contractform
        })
    else:
        return redirect('investors_signup')


@login_required
@user_referral_code_is_empty
def edit_contract(request):
    if request.user.investors_info.chosen_broker and request.user.investors_info.invest_amount:
        if request.method == 'POST':
            contractform = investors_forms.CreateContractForm(request.POST)
            if contractform.is_valid():
                contract = contractform.save(commit=False)
                contract.user = request.user
                contract.save()
                return redirect('add_new_contract')
    else:
        raise PermissionError
