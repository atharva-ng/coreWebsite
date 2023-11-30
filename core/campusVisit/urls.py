from django.urls import path

from .views import *

urlpatterns = [
    path('', campusVisitFront, name='campusVisitFront'),
]
