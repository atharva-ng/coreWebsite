from django.contrib import admin
from django.core.mail import send_mail
from django.conf import settings
from import_export.admin import ImportExportModelAdmin
import threading
from .models import *

# Register your models here.


def sendEmails(toEmails):
    subject = "Request Approved"
    message = "Content of the approved mail"
    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        toEmails,
        fail_silently=False
    )


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
                       "arrivialDate", "departureDate"]

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

            toEmails = []
            for alumni in alumnis:
                toEmails.append(alumni.email)

            # Mail Admin

            threading.Thread(
                target=sendEmails, name="Email Thread", args=(toEmails,)).start()

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
                       "arrivialDate", "departureDate"]


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
