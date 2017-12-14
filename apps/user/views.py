import requests
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .decorators import user_profile_is_empty
from .forms import SignUpForm, LoginForm, ProfileForm


# Create your views here.

def user_login(request):
    if request.user.is_authenticated and not request.user.is_anonymous:
        return redirect('user_home')
    else:
        if request.method == 'POST':
            loginform = LoginForm(data=request.POST)
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
            loginform = LoginForm()
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
                signupform = SignUpForm(request.POST)
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
        else:
            signupform = SignUpForm()
        return render(request, 'register.html', {'signupform': signupform})


@login_required
def user_logout(request):
    auth_logout(request)
    return redirect('/')


@login_required
@user_profile_is_empty
def user_home(request):
    return render(request, 'home.html', {
    })


@login_required
def user_profile(request):
    if request.method == 'POST':
        profileform = ProfileForm(request.POST, instance=request.user.profile)
        if profileform.is_valid():
            profileform.save()

        if request.user.profile.potential:
            return redirect('investors_signup')

    profileform = ProfileForm(instance=request.user.profile)
    return render(request, 'profile/profile.html', {'profileform': profileform})
