from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
import datetime
import threading

from django.http import JsonResponse

from .models import *
from .forms import contactForm
# Create your views here.


def frontPage(request):
    eventObjects = event.objects.order_by('date')[:4]
    print(eventObjects)
    context = {
        "events": eventObjects
    }
    return render(request, 'base/frontPage.html', context)


def aboutUs(request):
    context = {}
    return render(request, 'base/aboutUs.html', context)


def sendMail():
    subject = "Contact Request"
    message = "There is a new contact request."

    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        ['atharvaghadi4@gmail.com'],
        fail_silently=False
    )


def contact(request):
    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            form.save()

            email_thread = threading.Thread(
                target=sendMail, name="Email Thread")
            email_thread.start()

            messages.success(request, "submitted")

            context = {"form": contactForm()}
            context["message"] = "Form submitted successfully"
            return render(request, 'base/contact.html', context)
        else:
            context = {"form": form}
            context["form_errors"] = form.errors
            context["message"] = "Please resolve the errors"
            return render(request, 'base/contact.html', context)

    else:
        form = contactForm()
        context = {"form": form}

    return render(request, 'base/contact.html', context)


def eventView(request):
    current_year = datetime.datetime.now().year
    eventObjects = event.objects.filter(date__year=current_year)
    context = {"events": eventObjects,
               "currentYear": current_year,
               "prevYear": current_year-1}
    return render(request, 'base/events.html', context)


def scholarshipsView(request):
    context = {}
    return render(request, 'base/scholarships.html', context)
