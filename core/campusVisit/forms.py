from django import forms
from .models import campusVisitRequest


class dateTimeInput(forms.DateInput):
    input_type = "date"


class campusVisitRequestForm(forms.ModelForm):
    class Meta:
        model = campusVisitRequest
        widgets = {'datesFrom': dateTimeInput(),
                   'datesTo': dateTimeInput()}
        fields = ("name", "studentId", "email",
                  "phoneNumber", "reason", "datesFrom", "datesTo")
