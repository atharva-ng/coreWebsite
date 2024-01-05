from django import forms
from .models import *


class aluminiForm(forms.ModelForm):
    class Meta:
        model = alumni
        exclude = ['aluminiPK', 'visitRequestForm']


class guestForm(forms.ModelForm):
    class Meta:
        model = guest
        exclude = ['guestPK', 'relatedAlumni']


class visitReqForm:
    alumini_Form = aluminiForm()
    guest_Form = guestForm()

    class Meta:
        model = visitRequest
        exclude = ['requestPK', 'created', 'updated', 'valid']
