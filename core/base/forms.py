from django.forms import ModelForm
from .models import contactDetail


class contactForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['firstName'].widget.attrs.update({
            "class": "multisteps-form__input form-control",
            "type": "text",
            "required_id": "id_firstName",
            "placeholder": "First Name",
        })
        self.fields['firstName'].initial = ''

        self.fields['lastName'].widget.attrs.update({
            "class": "multisteps-form__input form-control",
            "type": "text",
            "required_id": "id_lastName",
            "placeholder": "Last Name",
        })
        self.fields['lastName'].initial = ''

        self.fields['email'].widget.attrs.update({
            "class": "multisteps-form__input form-control",
            "type": "email",
            "required_id": "id_email",
            "placeholder": "Email",
        })

        self.fields['phoneNumber'].widget.attrs.update({
            "class": "multisteps-form__input form-control",
            "type": "tel",
            "required_id": "id_phoneNumber",
            "placeholder": "Contact Number (+91 xxxxx xxxxx)",
        })

        self.fields['subject'].widget.attrs.update({
            "class": "multisteps-form__input form-control",
            "type": "text",
            "required_id": "id_subject",
            "placeholder": "Subject",
        })

        self.fields['message'].widget.attrs.update({
            "class": "form-control",
            "type": "text",
            "required_id": "id_message",
            "placeholder": "Message",
            "rows": "6"
        })

    class Meta:
        model = contactDetail
        fields = ("firstName", "lastName", "email",
                  "subject", "message", "phoneNumber")
