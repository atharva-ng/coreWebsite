from django import forms
from .models import *
from django.forms import TextInput


class DateInput(forms.DateInput):
    input_type = 'date'


class alumniForm(forms.ModelForm):
    required_css_class = 'required-field'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['firstName'].widget.attrs.update({
            "class": "multisteps-form__input form-control",
            "type": "text",
            "name": "Alumni-0-firstName",
            "id": "id_Alumni-0-firstName",
            "placeholder": "First Name",
        })
        self.fields['lastName'].widget.attrs.update({
            "class": "multisteps-form__input form-control",
            "type": "text",
            "name": "Alumni-0-lastName",
            "id": "id_Alumni-0-lastName",
            "placeholder": "Last Name",
        })
        self.fields['email'].widget.attrs.update({
            "class": "multisteps-form__input form-control",
            "type": "email",
            "name": "Alumni-0-email",
            "id": "id_Alumni-0-email",
            "placeholder": "Email",
        })

        self.fields['phoneNumber'].widget.attrs.update({
            "class": "multisteps-form__input form-control",
            "type": "tel",
            "name": "Alumni-0-phoneNumber",
            "id": "id_Alumni-0-phoneNumber",
            "placeholder": "Contact Number",
        })
        self.fields['BitsId'].widget.attrs.update({
            "class": "multisteps-form__input form-control",
            "type": "text",
            "name": "Alumni-0-BitsId",
            "id": "id_Alumni-0-BitsId",
            "placeholder": "BITS ID",
        })
        self.fields['purposeOfVisit'].widget.attrs.update({
            "class": "multisteps-form__input form-control",
            "type": "text",
            "name": "Alumni-0-purposeOfVisit",
            "id": "id_Alumni-0-purposeOfVisit",
            "placeholder": "Purpose of Visit",
        })
        self.fields['arrivialDate'].widget.attrs.update({
            "class": "multisteps-form__input form-control",
            "type": "date",
            "name": "Alumni-0-arrivialDate",
            "id": "id_Alumni-0-arrivialDate",
            "placeholder": "Arrival Date",
        })
        self.fields['currCompany'].widget.attrs.update({
            "class": "multisteps-form__input form-control",
            "type": "text",
            "name": "Alumni-0-currCompany",
            "id": "id_Alumni-0-currCompany",
            "placeholder": "Current Company",
        })
        self.fields['CompanyDesignation'].widget.attrs.update({
            "class": "multisteps-form__input form-control",
            "type": "text",
            "name": "Alumni-0-CompanyDesignation",
            "id": "Alumni-0-CompanyDesignation",
            "placeholder": "Designation in the Current Company",
        })
        self.fields['currAddress'].widget.attrs.update({
            "class": "multisteps-form__input form-control",
            "type": "text",
            "name": "Alumni-0-currAddress",
            "id": "id_Alumni-0-currAddress",
            "placeholder": "Current Address",
        })
        self.fields['zip'].widget.attrs.update({
            "class": "multisteps-form__input form-control",
            "type": "text",
            "name": "Alumni-0-zip",
            "id": "id_Alumni-0-zip",
            "placeholder": "ZIP",
        })
        self.fields['city'].widget.attrs.update({
            "class": "multisteps-form__input form-control",
            "type": "text",
            "name": "Alumni-0-city",
            "id": "id_Alumni-0-city",
            "placeholder": "City",
        })
        self.fields['country'].widget.attrs.update({
            "class": "multisteps-form__input form-control",
            "type": "text",
            "name": "Alumni-0-country",
            "id": "id_Alumni-0-country",
            "placeholder": "Country",
        })
        self.fields['state'].widget.attrs.update({
            "class": "multisteps-form__input form-control",
            "type": "text",
            "name": "Alumni-0-state",
            "id": "id_Alumni-0-state",
            "placeholder": "State",
        })

    # def clean(self):
    #     cleaned_data = super().clean()
    #     start_date = cleaned_data.get("start_date")
    #     end_date = cleaned_data.get("end_date")
    #     print("Called====================================================")
    #     if start_date and end_date:
    #         if start_date > end_date:
    #             raise forms.ValidationError(
    #                 "End date should be after start date.")
    #     return cleaned_data

    class Meta:
        model = alumni
        exclude = ['aluminiPK', 'visitRequestForm']
        widgets = {
            'arrivialDate': DateInput(),
            'zip': TextInput()
        }


class guestForm(forms.ModelForm):
    required_css_class = 'required-field'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['firstName'].widget.attrs.update({
            "class": "multisteps-form__input form-control",
            "type": "text",
            "name": "Guest-0-firstName",
            "id": "id_Guest-0-firstName",
            "placeholder": "First Name",
        })
        self.fields['lastName'].widget.attrs.update({
            "class": "multisteps-form__input form-control",
            "type": "text",
            "name": "Guest-0-lastName",
            "id": "id_Guest-0-lastName",
            "placeholder": "Last Name",
        })
        self.fields['email'].widget.attrs.update({
            "class": "multisteps-form__input form-control",
            "type": "email",
            "name": "Guest-0-email",
            "id": "id_Guest-0-email",
            "placeholder": "Email",
        })

        self.fields['phoneNumber'].widget.attrs.update({
            "class": "multisteps-form__input form-control",
            "type": "tel",
            "name": "Guest-0-phoneNumber",
            "id": "id_Guest-0-phoneNumber",
            "placeholder": "Contact Number",
        })

    class Meta:
        model = guest
        exclude = ['guestPK', 'relatedAlumni']
