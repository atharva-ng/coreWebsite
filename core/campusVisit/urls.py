from django.urls import path
from .views import campusVisitFront  # Import the donations view

urlpatterns = [
    path('', campusVisitFront, name='campusVisitFront'),  # Existing URL pattern

]
