from django import forms
from .models import *


class alumniForm(forms.ModelForm):
    class Meta:
        model = alumni
        exclude = ['aluminiPK', 'visitRequestForm']


class guestForm(forms.ModelForm):
    class Meta:
        model = guest
        exclude = ['guestPK', 'relatedAlumni']


class visitReqForm(forms.ModelForm):
    class Meta:
        model = visitRequest
        exclude = ['requestPK', 'created', 'updated', 'valid']
