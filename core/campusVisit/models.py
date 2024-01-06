from django.db import models
from datetime import datetime
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


class visitRequest(models.Model):
    requestPK = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    updated = models.DateTimeField(auto_now=True)
    valid = models.BooleanField(default=False)

    def __str__(self):
        dateTimeStr = self.created.strftime('%Y-%m-%d %H:%M:%S')
        return dateTimeStr


class alumni(models.Model):
    alumniPK = models.AutoField(primary_key=True)
    visitRequestForm = models.ForeignKey(
        visitRequest, on_delete=models.CASCADE, related_name='aluminis', null=False, blank=False)
    firstName = models.CharField(max_length=50, null=False, blank=False)
    lastName = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phoneNumber = PhoneNumberField()
    BitsId = models.CharField(max_length=13, null=False, blank=False)
    purposeOfVisit = models.CharField(max_length=254, null=False, blank=False)
    arrivialDateTime = models.DateTimeField(
        default=timezone.now, null=False, blank=False, verbose_name="From Date")
    departureDateTime = models.DateTimeField(
        default=timezone.now, null=False, blank=False, verbose_name="To Date")
    currCompany = models.CharField(
        max_length=254, null=False, blank=False, default="NONE")
    CompanyDesignation = models.CharField(
        max_length=254, null=False, blank=False, default="NONE")
    comingFrom = models.CharField(
        max_length=254, null=False, blank=False, default="NONE")
    currAddress = models.CharField(
        max_length=254, null=False, blank=False, default="NONE")

    def __str__(self):
        return self.firstName+self.lastName


class guest(models.Model):
    guestPK = models.AutoField(primary_key=True)
    relatedAlumni = models.ForeignKey(
        alumni, on_delete=models.CASCADE, related_name='guests')
    firstName = models.CharField(max_length=50, null=False, blank=False)
    lastName = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phoneNumber = PhoneNumberField()

    def __str__(self):
        return self.firstName+self.lastName
