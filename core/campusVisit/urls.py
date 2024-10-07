from django.urls import path
from .views import campusVisitFront, donations  # Import the donations view

urlpatterns = [
    path('', campusVisitFront, name='campusVisitFront'),  # Existing URL pattern
    path('donations/', donations, name='donations'),  # New URL pattern for donations
]
