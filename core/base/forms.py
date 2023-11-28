from django.forms import ModelForm
from .models import contactDetail


class contactForm(ModelForm):
    class Meta:
        model = contactDetail
        fields = ("name", "email", "subject", "message")
