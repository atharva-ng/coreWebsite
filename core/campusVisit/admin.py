from django.contrib import admin
from .models import *

# Register your models here.


class guestInline(admin.StackedInline):
    model = guest
    fields = [("firstName", "lastName"),
              ("email", "phoneNumber",)]
    extra = 0


class alumniInline(admin.StackedInline):
    model = alumni
    fields = [("firstName", "lastName"),
              ("email", "phoneNumber", "BitsId"),
              "purposeOfVisit",
              ("currCompany", "CompanyDesignation"),
              ("currAddress", "city", "state", "country", "zip"),
              ("arrivialDate", "departureDate")]
    extra = 0


class requestAdmin(admin.ModelAdmin):
    model = visitRequest
    list_display = ('created', "valid")
    list_filter = ("valid",)
    inlines = [alumniInline, guestInline]


admin.site.register(visitRequest, requestAdmin)
