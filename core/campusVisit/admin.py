from django.contrib import admin
from .models import *

# Register your models here.


class guestInline(admin.StackedInline):
    model = guest
    extra = 0

    def has_add_permission(self):
        return False

    # This will help you to disable delete functionaliyt
    # def has_delete_permission(self, obj=None):
    #     return False


class alumniInline(admin.StackedInline):
    model = alumni
    extra = 0

    # def has_add_permission(self):
    #     return False

    # def has_delete_permission(self, obj=None):
    #     return False


class requestAdmin(admin.ModelAdmin):
    inlines = [alumniInline, guestInline]


admin.site.register(visitRequest, requestAdmin)
admin.site.register(alumni)
admin.site.register(guest)
