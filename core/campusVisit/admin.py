from django.contrib import admin
from django.core.mail import send_mail
from django.conf import settings
from import_export.admin import ImportExportModelAdmin
import threading
from .models import *
import datetime

# Register your models here.


def sendEmails(toEmails, alumniNameList, guestNameList, visitRequest):
    subject = "Campus Visit Request Approved"
    
    message = f"""Dear Alumni,

We are pleased to inform you that your campus visit request has been approved. We look forward to welcoming you to our campus.

Visit Details:
{'-' * 50}
"""

    for alumni in alumniNameList:
        message += f"""
Visitor: {alumni.firstName} {alumni.lastName}
BITS ID: {alumni.BitsId}
Time of Visit: {alumni.arrivalDate.strftime('%I:%M %p, %d %B %Y')}
Duration: {alumni.purposeOfVisit}
Contact Number: {alumni.phoneNumber}
Address: {alumni.currAddress}, {alumni.city}, {alumni.state}, {alumni.country}, {alumni.zip}

"""

    if guestNameList:
        message += f"\nAccompanying Guests:\n{'-' * 50}\n"
        for guest in guestNameList:
            message += f"""
Guest Name: {guest.firstName} {guest.lastName}
Contact Number: {guest.phoneNumber}

"""

    message += f"""
Important Information:
{'-' * 50}
1. Please carry a valid ID proof for verification at the gate.
2. Kindly adhere to all Institutional and COVID-appropriate norms throughout your visit.
3. Join AlmaConnect by visiting: https://bitspilani.almaconnect.com

If you have any queries, please don't hesitate to contact us.

We wish you a pleasant and memorable visit to your alma mater.

Best regards,
Alumni Relations Division
BITS Pilani K.K. Birla Goa Campus"""

    toEmails.extend(["ad.ar@goa.bits-pilani.ac.in", "cso@goa.bits-pilani.ac.in", "security@goa.bits-pilani.ac.in", "sarc@goa.bits-pilani.ac.in"])

    try:
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            toEmails,
            fail_silently=False
        )
    except Exception as e:
        alumEmails = ",".join(toEmails)
        with open("errorFiles/emailErrorsCampusVisit.txt", 'a') as file:
            file.write(f"{datetime.datetime.now()} {str(e)} sendMailToAlumni Emails: {alumEmails}\n")


class guestInline(admin.StackedInline):
    model = guest
    readonly_fields = ["firstName", "lastName",
                       "email", "phoneNumber",]
    extra = 0

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class alumniInline(admin.StackedInline):
    model = alumni
    extra = 0
    readonly_fields = ["firstName", "lastName",
                       "email", "phoneNumber", "BitsId",
                       "purposeOfVisit",
                       "currCompany", "CompanyDesignation",
                       "currAddress", "city", "state", "country", "zip",
                       "arrivalDate"]

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class requestAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    model = visitRequest
    list_display = ('requestPK', 'created', 'valid')
    list_filter = ("valid",)
    readonly_fields = ['requestPK', 'created']
    fields = ['valid']
    inlines = [alumniInline, guestInline]

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_import_permission(self, request):
        return False

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def save_model(self, request, obj, form, change):
        oldObj = self.model.objects.get(pk=obj.pk)
        if obj.valid and not oldObj.valid:
            alumnis = oldObj.aluminis.all()
            guests = oldObj.guests.all()

            toEmails = []
            alumniNameList = []
            guestNameList = []
            for alumni in alumnis:
                toEmails.append(alumni.email)
                alumniNameList.append(alumni)

            for guest in guests:
                guestNameList.append(guest)
            # Mail Admin

            threading.Thread(
                target=sendEmails, name="Email Thread", args=(toEmails, alumniNameList, guestNameList, oldObj)
            ).start()

            self.fields = []
            return super().save_model(request, obj, form, change)
        else:
            pass


admin.site.register(visitRequest, requestAdmin)


class alumniAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    model = alumni
    list_display = ('alumniPK', 'firstName', 'lastName', 'BitsId')

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return True

    def has_import_permission(self, request):
        return False

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    readonly_fields = ["visitRequestForm", "firstName", "lastName",
                       "email", "phoneNumber", "BitsId",
                       "purposeOfVisit",
                       "currCompany", "CompanyDesignation",
                       "currAddress", "city", "state", "country", "zip",
                       "arrivalDate"]


admin.site.register(alumni, alumniAdmin)


class guestAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    model = guest
    list_display = ["guestPK", "firstName", "lastName"]

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_import_permission(self, request):
        return False


admin.site.register(guest, guestAdmin)
