from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import *
from .forms import contactForm
# Create your views here.


def frontPage(request):
    return render(request, 'base/frontPage.html')


def aboutUs(request):
    cordis = coordi.objects.all()
    context = {'cordiLsObj': cordis}
    return render(request, 'base/aboutUs.html', context)


def contact(request):
    submitted = False
    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/contact?submitted=True")
    else:
        form = contactForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'base/contact.html', {"form": form, 'submitted': submitted})


def blogs(request):
    blogs = blog.objects.all()
    print(blogs)
    return render(request, 'base/blog.html', {"blogs": blogs})
