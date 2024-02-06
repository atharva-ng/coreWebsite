from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *
from .forms import contactForm
# Create your views here.


def frontPage(request):
    return render(request, 'base/frontPage.html')


def aboutUs(request):
    # cordis = coordi.objects.all()
    context = {}  # {'cordiLsObj': cordis}
    return render(request, 'base/aboutUs.html', context)


def contact(request):
    if request.method == 'POST':
        # print("==============================post")
        for data in request.POST.items():
            print(data)

        form = contactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("contact"))

    else:
        form = contactForm()
    context = {"form": form}
    return render(request, 'base/contact.html', context)


def blogs(request):
    blogs = blog.objects.all()
    print(blogs)
    return render(request, 'base/blog.html', {"blogs": blogs})


def eventView(request):
    eventObjects = event.objects.all()
    context = {"events": eventObjects}
    return render(request, 'base/events.html', context)
