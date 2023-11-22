from django.shortcuts import render, redirect
from .models import *
# Create your views here.


def frontPage(request):
    return render(request, 'base/frontPage.html')


def aboutUs(request):
    cordis = cordi.objects.all()
    context = {'cordiLsObj': cordis}
    return render(request, 'base/aboutUs.html', context)


def contact(request):
    return render(request, 'base/contact.html')
