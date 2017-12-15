import requests
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout as auth_logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from . import forms as user_forms
from .decorators import user_referral_code_is_empty


# Create your views here.

def user_login(request):
    if request.user.is_authenticated and not request.user.is_anonymous:
        return redirect('user_home')
    else:
        if request.method == 'POST':
            loginform = user_forms.LoginForm(data=request.POST)
            if loginform.is_valid():
                username = loginform.cleaned_data.get('username')
                raw_password = loginform.cleaned_data.get('password')
                user = authenticate(request, username=username, password=raw_password)
                if user is not None:
                    login(request, user)
                    return redirect('user_home')
                else:
                    return render(request, 'login.html', {'loginform': loginform})
        else:
            loginform = user_forms.LoginForm()
        return render(request, 'login.html', {'loginform': loginform})


def user_register(request):
    if request.user.is_authenticated and not request.user.is_anonymous:
        return redirect('user_home')
    else:
        if request.method == 'POST':
            recaptcha = request.POST.get('g-recaptcha-response')
            r = requests.post('https://www.google.com/recaptcha/api/siteverify', {
                "response": recaptcha,
                "secret": "6LfIfDwUAAAAALRY0xoOCIFiPTdHHqD-avJ3M7EJ"
            })
            if r.json()['success'] is True:
                signupform = user_forms.SignUpForm(request.POST)
                if signupform.is_valid():
                    signupform.save()
                    username = signupform.cleaned_data.get('username')
                    raw_password = signupform.cleaned_data.get('password1')
                    user = authenticate(username=username, password=raw_password)
                    if user is not None:
                        login(request, user)
                        return redirect('user_home')
                    else:
                        return render(request, 'register.html', {'signupform': signupform})
        signupform = user_forms.SignUpForm()
        return render(request, 'register.html', {'signupform': signupform})


@login_required
def user_logout(request):
    auth_logout(request)
    return redirect('/')


@login_required
@user_referral_code_is_empty
def user_home(request):
    return render(request, 'home.html', {
    })


@login_required
def account_settings_password(request):
    if request.user.has_usable_password():
        password_form = user_forms.PasswordChangeCustomForm
    else:
        password_form = user_forms.AdminPasswordChangeCustomForm

    if request.method == 'POST':
        form = password_form(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('user_settings_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = password_form(request.user)
    return render(request, 'profile/password.html', {'form': form})


@login_required
def user_next_step(request):
    if not request.user.profile.referral_code:
        if request.method == 'POST':
            signupnextstep = user_forms.SignupNextStep(request.POST, instance=request.user.profile)
            if signupnextstep.is_valid():
                signupnextstep.save()

            if request.user.profile.potential:
                return redirect('investors_signup')

        signupnextstep = user_forms.SignupNextStep(instance=request.user.profile)
        nameform = user_forms.UserForm(instance=request.user)
        return render(request, 'profile/user_step2.html', {
            'signupnextstep': signupnextstep,
            'nameform': nameform
        })
    else:
        return redirect('investors_index')
