from django.contrib import admin
from .models import SummerResearchApplication

@admin.register(SummerResearchApplication)
class SummerResearchApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'id_number', 'email', 'submitted_at', 'status')
    list_filter = ('status', 'submitted_at')
    search_fields = ('name', 'id_number', 'email')