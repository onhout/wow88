from django.shortcuts import redirect


def user_referral_code_is_empty(function):
    def wrap(request, *args, **kwargs):
        if request.user.profile.referral_code:
            return function(request, *args, **kwargs)  # this line means continue with the function
        else:
            return redirect('user_next_step')

    return wrap


def user_is_investor(function):
    def wrap(request, *args, **kwargs):
        if request.user.profile.referral_code and not request.user.profile.potential and request.user.profile.type == 'investor' or request.user.profile.type == 'both':
            return function(request, *args, **kwargs)  # this line means continue with the function
        else:
            return redirect('investors_signup')

    return wrap


def user_is_salesperson(function):
    def wrap(request, *args, **kwargs):
        if request.user.profile.referral_code and not request.user.profile.potential and request.user.profile.type == 'salesperson' or request.user.profile.type == 'both':
            return function(request, *args, **kwargs)  # this line means continue with the function
        else:
            return redirect('salesperson_signup')

    return wrap
