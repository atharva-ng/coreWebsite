from django.contrib import admin
from .models import *

# Register your models here.


class guestInline(admin.StackedInline):
    model = guest
    extra = 1


class alumniInline(admin.StackedInline):
    model = alumni
    inlines = [guestInline]
    extra = 1


class requestAdmin(admin.ModelAdmin):
    inlines = [alumniInline]


admin.site.register(visitRequest, requestAdmin)
admin.site.register(alumni)
admin.site.register(guest)
