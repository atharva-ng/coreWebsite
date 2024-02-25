from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings

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
        form = contactForm(request.POST)

        if form.is_valid():
            form.save()
            # Mail Admin
            subject = "Contact Request"
            message = "There is a new contact request."

            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                # [request.POST.get('email')],
                ['atharvaghadi4@gmail.com'],
                fail_silently=False
            )

            messages.success(request, "submitted")
            return redirect(reverse('contact'))
        else:
            context = {"form": form}
            return render(request, 'base/contact.html', context)

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
