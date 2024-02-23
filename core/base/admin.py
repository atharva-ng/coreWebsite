from django.contrib import admin
from .models import *


class contactAdmin(admin.ModelAdmin):
    fields = [("firstName", "lastName"), ("email", "phoneNumber"),
              "subject", "message", "contacted"]

    list_display = ('sno', "firstName", "lastName", "contacted")
    list_filter = ("contacted",)


class eventAdmin(admin.ModelAdmin):
    pass


admin.site.register(contactDetail, contactAdmin)
admin.site.register(event, eventAdmin)
