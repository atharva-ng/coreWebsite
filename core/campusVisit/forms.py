from django import forms
from .models import *


class alumniForm(forms.ModelForm):
    required_css_class = 'required-field'

    class Meta:
        model = alumni
        exclude = ['aluminiPK', 'visitRequestForm']


class guestForm(forms.ModelForm):
    class Meta:
        model = guest
        exclude = ['guestPK', 'relatedAlumni']
