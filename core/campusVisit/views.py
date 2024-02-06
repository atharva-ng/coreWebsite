from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.forms import inlineformset_factory
from .forms import *
from .models import visitRequest, alumni

# Create your views here.


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

    alumniFormSet = alumniFormSetClass(prefix='Alumni')

    guestFormSet = guestFormSetClass(prefix='Guest')
    context = {
        "alumniFormSet": alumniFormSet,
        "guestFormSet": guestFormSet
    }

    return render(request, 'campusVisitFront.html', context)
