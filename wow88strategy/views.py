from django.shortcuts import render, redirect


# Create your views here.

def login(request):
    if request.user.is_authenticated and not request.user.is_anonymous:
        return redirect('user_home')
    else:
        return render(request, 'index.html', {
        })


def user_home(request):
    return render(request, 'index.html', {
    })
