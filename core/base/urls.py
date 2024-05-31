from django.urls import path

from .views import *

urlpatterns = [
    path('', frontPage, name='frontPage'),
    path('about', aboutUs, name='aboutUs'),
    path('contact/', contact, name='contact'),
    path('events/', eventView, name="events"),
    path('scholarships/', scholarshipsView, name="scholarships"),
    path('scholarshipDetails/<str:scName>',
         scholarshipsViewDetails, name="scholarshipDetails"),
]

handler404 = 'base.views.handler404'
