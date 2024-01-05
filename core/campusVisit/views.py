from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import *

# from .models import *
# from .forms import campusVisitRequestForm

# Create your views here.


def campusVisitFront(request):
    if request.method == 'POST':
        print("==================POST==================")
    else:
        form = visitReqForm()

    return render(request, 'campusVisitFront.html', {"form": form})
