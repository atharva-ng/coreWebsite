from django.shortcuts import render, redirect

# Create your views here.


def frontPage(request):
    return render(request, 'base/frontPage.html')


def aboutUs(request):
    return render(request, 'base/aboutUs.html')


def contact(request):
    return render(request, 'base/contact.html')
