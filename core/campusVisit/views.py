from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import *
from .models import visitRequest

# Create your views here.


def campusVisitFront(request):
    if request.method == 'POST':
        alumniDetails = alumniForm(request.POST)
        guestDetails = guestForm(request.POST)
        if alumniDetails.is_valid() and guestDetails.is_valid():
            formInstance = visitRequest()
            formInstance.save()

            alumniInstance = alumniDetails.save(commit=False)
            alumniInstance.visitRequestForm = formInstance

            guestInstance = guestDetails.save(commit=False)
            guestInstance.relatedAlumni = alumniInstance

            alumniInstance.save()
            guestInstance.save()
            submitted = True

    alumniFormView = alumniForm()
    guestFormView = guestForm()
    context = {"alumniFormView": alumniFormView,
               "guestFormView": guestFormView}
    return render(request, 'campusVisitFront.html', context)
