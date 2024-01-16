from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.forms import formset_factory, inlineformset_factory
from .forms import *
from .models import visitRequest

# Create your views here.


def campusVisitFront(request):
    if request.method == 'POST':
        alumniFormSetClass = formset_factory(alumniForm, extra=1)
        # guestFormSetClass = inlineformset_factory(
        #     alumni, guest, form=guestForm, extra=1)

        alumniFormSet = alumniFormSetClass(request.POST, prefix='Alumni')
        # guestFormSet = guestFormSetClass(request.POST, prefix='Guest')

        if alumniFormSet.is_valid():  # and guestFormSet.is_valid():
            formInstance = visitRequest()
            formInstance.save()
            alumniFormSetInstances = alumniFormSet.save(commit=False)
            # guestFormSetInstances = guestFormSet.save(commit=False)
            for alumniFormInstance in alumniFormSetInstances:
                alumniFormInstance.visitRequestForm = formInstance
                alumniFormInstance.save()
        return HttpResponseRedirect(request, 'campusVisitFront.html')
    else:
        alumniFormSetClass = formset_factory(alumniForm, extra=1)
        # guestFormSetClass = inlineformset_factory(
        #     alumni, guest, form=guestForm, extra=1)
        alumniFormSet = alumniFormSetClass(prefix='Alumni')
        # guestFormSet = guestFormSetClass(prefix='Guest')

        context = {
            "alumniFormSet": alumniFormSet,
            # "guestFormSet": guestFormSet
        }

    return render(request, 'campusVisitFront.html', context)


# def campusVisitFront(request):
#     if request.method == 'POST':
#         alumniDetails = alumniForm(request.POST)
#         guestDetails = guestForm(request.POST)
#         if alumniDetails.is_valid() and guestDetails.is_valid():
#             formInstance = visitRequest()
#             formInstance.save()

#             alumniInstance = alumniDetails.save(commit=False)
#             alumniInstance.visitRequestForm = formInstance

#             guestInstance = guestDetails.save(commit=False)
#             guestInstance.relatedAlumni = alumniInstance

#             alumniInstance.save()
#             guestInstance.save()

#     alumniFormView = alumniForm()
#     guestFormView = guestForm()
#     context = {"alumniFormView": alumniFormView,
#                "guestFormView": guestFormView}
#     return render(request, 'campusVisitFront.html', context)
