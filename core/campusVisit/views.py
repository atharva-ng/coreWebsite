from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import *
from .forms import campusVisitRequestForm

# Create your views here.


def campusVisitFront(request):
    submitted = False
    if request.method == 'POST':
        form = campusVisitRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/campusVisit?submitted=True")
    else:
        form = campusVisitRequestForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'campusVisitFront.html', {"form": form, 'submitted': submitted})
