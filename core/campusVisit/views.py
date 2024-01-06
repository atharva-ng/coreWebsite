from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import *

# from .models import *
# from .forms import campusVisitRequestForm

# Create your views here.


def campusVisitFront(request):
    submitted = False
    if request.method == 'POST':
        alumniDetails = alumniForm(request.POST)
        guestDetails = guestForm(request.POST)
        if alumniDetails.is_valid() and guestDetails.is_valid():
            visitDetails = visitReqForm(request.POST)
            print(visitDetails.is_valid())

            instance = visitDetails.save(commit=False)
            instance.created = datetime.now()
            instance.save()
            alumniDetails.save(commit=False)
            alumniDetails.visitRequestForm = visitDetails
            alumniDetails.save()
            guestDetails.save(commit=False)
            guestDetails.relatedAlumni = alumniDetails
            guestDetails.save()
        submitted = True

    alumniFormView = alumniForm()
    guestFormView = guestForm()
    context = {"alumniFormView": alumniFormView,
               "guestFormView": guestFormView, 'submitted': submitted}
    return render(request, 'campusVisitFront.html', context)
