# core/scholarship/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('apply/', views.scholarship_form, name='scholarship_form'),
    path('success/', views.summer_research_application_success, name='summer_research_application_success'),
]
