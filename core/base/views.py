from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
import datetime
import threading

from .models import *
from .forms import contactForm
# Create your views here.


def frontPage(request):
    try:
        eventObjects0 = event.objects.order_by('date')
        if len(eventObjects0) < 4:
            eventObjects = eventObjects0
        else:
            eventObjects = eventObjects0[::-1][:4]

        context = {
            "events": eventObjects
        }

    except Exception as e:
        with open("errorFiles/generalErrors.txt", 'a') as file:
            file.write(str(datetime.datetime.now())+" " +
                       str(e)+" " + "FrontPageView "+'\n')
        eventObjects = []
        context = {
            "events": eventObjects
        }
    finally:
        return render(request, 'base/frontPage.html', context)


def aboutUs(request):
    context = {}
    return render(request, 'base/aboutUs.html', context)


def sendMail():
    subject = "Contact Request"
    message = "There is a new contact request."
    try:
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            ['atharvaghadi4@gmail.com']
        )
    except Exception as e:
        with open("emailErrorsContact.txt", 'a') as file:
            file.write(str(datetime.datetime.now())+" " +
                       str(e)+" " + "sendMailContactView "+'\n')


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
    try:
        eventObjects = event.objects.filter(date__year=current_year)[::-1]
    except Exception as e:
        with open("errorFiles/generalErrors.txt", 'a') as file:
            file.write(str(datetime.datetime.now())+" " +
                       str(e)+" " + "EventView "+'\n')
        eventObjects = []
    context = {"events": eventObjects,
               "currentYear": current_year,
               "prevYear": current_year-1}
    return render(request, 'base/events.html', context)


def scholarshipsView(request):

    context = {}
    return render(request, 'base/scholarships.html', context)


def scholarshipsViewDetails(request, scName):
    return render(request, f'base/scholarshipDetails/{scName}.html')


# def handler404(request, exception, template_name='404.html'):
#     response = render_to_response(template_name)
#     response.status_code = 404
#     return response
