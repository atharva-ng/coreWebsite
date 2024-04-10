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
    try:
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            ["atharvaghadi4@gmail.com"]
        )
    except Exception as e:
        with open("emailErrorsContact.txt", 'a') as file:
            file.write(str(datetime.datetime.now())+" " +
                       str(e)+" " + "sendMailToAdmin "+'\n')


def campusVisitFront(request):
    alumniFormSetClass = inlineformset_factory(
        visitRequest, alumni, form=alumniForm, max_num=5, extra=0, min_num=1)

    guestFormSetClass = inlineformset_factory(
        visitRequest, guest, form=guestForm, extra=1, max_num=5, min_num=0)

    if request.method == 'POST':
        alumniFormSet = alumniFormSetClass(
            request.POST, prefix='Alumni')

        guestFormSet = guestFormSetClass(
            request.POST, prefix='Guest')
        if alumniFormSet.is_valid() and guestFormSet.is_valid():
            formInstance = visitRequest()
            formInstance.save()

            emailList = []
            nameList = []

            alumniFormSetInstances = alumniFormSet.save(commit=False)
            for alumniFormInstance in alumniFormSetInstances:
                alumniFormInstance.visitRequestForm = formInstance
                emailList.append(alumniFormInstance.email)
                nameList.append(alumniFormInstance)
                alumniFormInstance.save()

            guestFormSetInstances = guestFormSet.save(commit=False)
            for guestFormSetInstance in guestFormSetInstances:
                nameList.append(guestFormSetInstance)
                guestFormSetInstance.visitRequestForm = formInstance
                guestFormSetInstance.save()

            threading.Thread(
                target=sendEmails, args=(emailList, nameList), name="Email Thread").start()

            data = {}
            return JsonResponse(data, status=200)
        else:
            errorList = []

            for form in alumniFormSet:
                for field, error in form.errors.items():
                    if field+": "+error not in errorList:
                        errorList.append(field+": "+error)

            for form in guestFormSet:

                for field, error in form.errors.items():
                    if field+": "+error not in errorList:
                        errorList.append(field+": "+error)

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
        return HttpResponse(status=400)
