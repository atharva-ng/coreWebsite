from django.contrib import admin
from .models import *


class contactAdmin(admin.ModelAdmin):
    fields = [("firstName", "lastName"), ("email", "phoneNumber"),
              "subject", "message", "contacted"]

    list_display = ('sno', "firstName", "lastName", "contacted")
    list_filter = ("contacted",)

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


class eventAdmin(admin.ModelAdmin):
    pass


admin.site.register(contactDetail, contactAdmin)
admin.site.register(event, eventAdmin)
