from django import forms
from .models import *


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
        self.fields['arrivialDateTime'].widget.attrs.update({
            "class": "multisteps-form__input form-control",
            "type": "text",
            "name": "Alumni-0-arrivialDateTime",
            "id": "id_Alumni-0-arrivialDateTime",
            "placeholder": "Arrival Datetime",
        })
        self.fields['departureDateTime'].widget.attrs.update({
            "class": "multisteps-form__input form-control",
            "type": "text",
            "name": "Alumni-0-departureDateTime",
            "id": "id_Alumni-0-departureDateTime",
            "placeholder": "Departure DateTime",
        })
        self.fields['currCompany'].widget.attrs.update({
            "class": "multisteps-form__input form-control",
            "type": "text",
            "name": "Alumni-0-currCompany",
            "id": "id_Alumni-0-currCompany",
            "placeholder": "BITS ID",
        })
        self.fields['CompanyDesignation'].widget.attrs.update({
            "class": "multisteps-form__input form-control",
            "type": "text",
            "name": "Alumni-0-CompanyDesignation",
            "id": "Alumni-0-CompanyDesignation",
            "placeholder": "BITS ID",
        })
        self.fields['comingFrom'].widget.attrs.update({
            "class": "multisteps-form__input form-control",
            "type": "text",
            "name": "Alumni-0-comingFrom",
            "id": "id_Alumni-0-comingFrom",
            "placeholder": "BITS ID",
        })
        self.fields['currAddress'].widget.attrs.update({
            "class": "multisteps-form__input form-control",
            "type": "text",
            "name": "Alumni-0-currAddress",
            "id": "id_Alumni-0-currAddress",
            "placeholder": "BITS ID",
        })

    class Meta:
        model = alumni
        exclude = ['aluminiPK', 'visitRequestForm']


class guestForm(forms.ModelForm):
    class Meta:
        model = guest
        exclude = ['guestPK', 'relatedAlumni']
