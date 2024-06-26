from django import forms
from .models import *
from django.forms import TextInput
from phonenumber_field.formfields import PhoneNumberField


class DateInput(forms.DateInput):
    input_type = 'date'


class alumniForm(forms.ModelForm):
    required_css_class = 'required-field'
    phoneNumber = PhoneNumberField(
        error_messages={'invalid': "Enter a valid Contact Number (+91 xxxxx xxxxx)."})

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
        self.fields['arrivalDate'].widget.attrs.update({
            "class": "multisteps-form__input form-control",
            "type": "date",
            "name": "Alumni-0-arrivalDate",
            "id": "id_Alumni-0-arrivalDate",
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
            "id": "id_Alumni-0-CompanyDesignation",
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

    class Meta:
        model = alumni
        exclude = ['aluminiPK', 'visitRequestForm']
        widgets = {
            'arrivalDate': DateInput(),
            'zip': TextInput()
        }

    def clean(self):
        cleaned_data = super().clean()

        readonly_fields = ["firstName", "lastName",
                           "email", "phoneNumber", "BitsId",
                           "purposeOfVisit",
                           "currCompany", "CompanyDesignation",
                           "currAddress", "city", "state", "country", "zip",
                           ]
        error_messages = {
            'firstName': {
                'blank': ('First Name Cannot be empty.'),
            },
            'lastName': {
                'blank': ('Last Name cannot be empty.'),
            },
            'email': {
                'blank': ('Please enter your Email address.'),
            },
            'phoneNumber': {
                'blank': ('Please enter your Phone number'),
            },
            'BitsId': {
                'blank': ('Please enter your BITS Id'),
            },
            'purposeOfVisit': {
                'blank': ('Please enter the purpose of this visit'),
            },
            'currCompany': {
                'blank': ('Please enter your current place of employment'),
            },
            'CompanyDesignation': {
                'blank': ('Please enter your designation in your company.'),
            },
            'currAddress': {
                'blank': ('Please enter your current address'),
            },
            'city': {
                'blank': ('Please enter your City'),
            },
            'state': {
                'blank': ('Please enter your State'),
            },
            'country': {
                'blank': ('Please enter your country'),
            },
            'zip': {
                'blank': ('Please enter your ZIP code'),
            },
            'arrivalDate': {
                'blank': ("Please enter the arrival date."),
            }
        }

        for field in readonly_fields:
            data = cleaned_data.get(field)
            if data == None:
                if self.errors[field][0] == "This field is required.":
                    self.errors[field][0] = error_messages[field]['blank']
                elif self.errors[field][0] == "Enter a whole number.":
                    self.errors[field][0] = "Zip Code should not be alphanumeric or have special characters."

        data = cleaned_data.get("arrivalDate")
        if data == None:
            self.errors["arrivalDate"][0] = error_messages["arrivalDate"]['blank']

        return cleaned_data


class guestForm(forms.ModelForm):
    required_css_class = 'required-field'
    phoneNumber = PhoneNumberField(
        error_messages={'invalid': "Guest-Enter a valid Contact Number (+91 xxxxx xxxxx)."})

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

    def clean(self):
        cleaned_data = super().clean()

        readonly_fields = ["firstName", "lastName",
                           "email", "phoneNumber",
                           ]
        error_messages = {
            'firstName': {
                'blank': ('Guest-First Name Cannot be empty.'),
            },
            'lastName': {
                'blank': ('Guest-Last Name cannot be empty.'),
            },
            'email': {
                'blank': ('Guest-Please enter your Email address.'),
            },
            'phoneNumber': {
                'blank': ('Guest-Please enter your Phone number'),
            },
        }

        for field in readonly_fields:
            data = cleaned_data.get(field)
            if data == None:
                if self.errors[field][0] == "This field is required.":
                    self.errors[field][0] = error_messages[field]['blank']
        return cleaned_data
