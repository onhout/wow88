import requests
from django.shortcuts import render, redirect


# Create your views here.

def index_page(request):
    return render(request, 'index.html', {})


def contact_us_message(request):
    recaptcha = request.POST.get('g-recaptcha-response')
    r = requests.post('https://www.google.com/recaptcha/api/siteverify', {
        "response": recaptcha,
        "secret": "6LfIfDwUAAAAALRY0xoOCIFiPTdHHqD-avJ3M7EJ"
    })
    if request.method == "POST" and request.POST.get('email') and r.json()['success'] is True:
        print('sent')
        return redirect('index_page')
    return redirect('index_page')
