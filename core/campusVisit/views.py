from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest
from django.core.mail import send_mail
from django.forms import inlineformset_factory
from django.conf import settings

from .forms import *
from .models import visitRequest, alumni

# Create your views here.


def sendEmails(subject, message):
    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        ['atharvaghadi4@gmail.com'],
        fail_silently=False
    )


def campusVisitFront(request):
    alumniFormSetClass = inlineformset_factory(
        visitRequest, alumni, form=alumniForm, extra=0, max_num=5, min_num=1)

    guestFormSetClass = inlineformset_factory(
        visitRequest, guest, form=guestForm, extra=1, max_num=5, min_num=0)

    if request.method == 'POST':
        alumniFormSet = alumniFormSetClass(
            request.POST, prefix='Alumni')

        guestFormSet = guestFormSetClass(
            request.POST, prefix='Guest')

        if alumniFormSet.is_valid() and guestFormSet.is_valid():
            print("===================valid=======================")
            formInstance = visitRequest()
            formInstance.save()
            alumniFormSetInstances = alumniFormSet.save(commit=False)
            for alumniFormInstance in alumniFormSetInstances:
                alumniFormInstance.visitRequestForm = formInstance
                alumniFormInstance.save()

            guestFormSetInstances = guestFormSet.save(commit=False)
            for guestFormSetInstance in guestFormSetInstances:
                guestFormSetInstance.visitRequestForm = formInstance
                guestFormSetInstance.save()

            subject = "Campus visit Request"
            message = "There is a new Campus visit request."
            sendEmails(subject, message)

            return redirect('campusVisitFront')
        else:
            context = {
                "alumniFormSet": alumniFormSet,
                "guestFormSet": guestFormSet,
            }
            return HttpResponseBadRequest()
            # return render(request, 'campusVisitFront.html', context)
    elif request.method == 'GET':
        alumniFormSet = alumniFormSetClass(prefix='Alumni')

        guestFormSet = guestFormSetClass(prefix='Guest')
        context = {
            "alumniFormSet": alumniFormSet,
            "guestFormSet": guestFormSet
        }

        return render(request, 'campusVisitFront.html', context)
    elif request.method == "HEAD":
        response = HttpResponse()
        return response
    else:
        return HttpResponse(status=405)
