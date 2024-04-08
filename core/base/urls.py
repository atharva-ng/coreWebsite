from django.urls import path

from .views import *

urlpatterns = [
    path('', frontPage, name='frontPage'),
    path('about', aboutUs, name='aboutUs'),
    path('contact/', contact, name='contact'),
    path('blogs', blogs, name='blogs'),
    path('events/', eventView, name="events"),
    path('scholarships/', scholarshipsView, name="scholarships"),
]
