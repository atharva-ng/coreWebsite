from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest
from django.core.mail import send_mail
from django.forms import inlineformset_factory
from django.conf import settings
import threading
import json

from .forms import *
from .models import visitRequest, alumni

# Create your views here.


def sendEmails():
    subject = "Campus visit Request"
    message = "There is a new Campus visit request."
    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        ['atharvaghadi4@gmail.com'],
        fail_silently=False
    )


def campusVisitFront(request):
    alumniFormSetClass = inlineformset_factory(
        visitRequest, alumni, form=alumniForm, extra=0, min_num=1)

    guestFormSetClass = inlineformset_factory(
        visitRequest, guest, form=guestForm, extra=1, max_num=5, min_num=0)

    if request.method == 'POST':
        alumniFormSet = alumniFormSetClass(
            request.POST, prefix='Alumni')

        guestFormSet = guestFormSetClass(
            request.POST, prefix='Guest')
        print("======================================")
        print(request.POST)
        print("======================================")
        print(alumniFormSet)
        print("======================================")
        if alumniFormSet.is_valid() and guestFormSet.is_valid():
            print("===================valid=======================")

            formInstance = visitRequest()
            formInstance.save()
            alumniFormSetInstances = alumniFormSet.save(commit=False)
            for alumniFormInstance in alumniFormSetInstances:
                print("======================================")
                print(alumniFormInstance)
                print("======================================")
                alumniFormInstance.visitRequestForm = formInstance
                alumniFormInstance.save()

            guestFormSetInstances = guestFormSet.save(commit=False)
            for guestFormSetInstance in guestFormSetInstances:
                guestFormSetInstance.visitRequestForm = formInstance
                guestFormSetInstance.save()

            threading.Thread(
                target=sendEmails, name="Email Thread").start()

            data = {}
            return JsonResponse(data, status=200)
        else:
            errorList = []
            for form in alumniFormSet:
                for field, error in form.errors.items():
                    errorList.append(error[0])

            alumniFormSet = alumniFormSetClass(
                request.POST, prefix='Alumni')

            guestFormSet = guestFormSetClass(
                request.POST, prefix='Guest')
            context = {
                "errors": errorList,
            }
            serializedContext = json.dumps(context)
            print(serializedContext)
            return JsonResponse({"errors": serializedContext}, status=402)

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
