from django.db import models
from datetime import datetime
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField

from django.core.validators import EmailValidator, RegexValidator
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
    email = models.EmailField(max_length=254, null=False, blank=False, validators=[
                              EmailValidator(message='You have entered an invalid email address')])
    phoneNumber = PhoneNumberField()
    BitsId = models.CharField(max_length=13, null=False, blank=False, validators=[RegexValidator(
        regex=r'^\d{4}[A-Z0-9]{2}[A-Z0-9]{2}\d{4}[A-Z]+$', message="Enter a valid BITS ID(20##XXPS####G)")])
    purposeOfVisit = models.CharField(max_length=254, null=False, blank=False)
    arrivalDate = models.DateTimeField(
        null=False, blank=False, verbose_name="From Date")
    currCompany = models.CharField(
        max_length=254, null=False, blank=False)
    CompanyDesignation = models.CharField(
        max_length=254, null=False, blank=False)
    currAddress = models.CharField(
        max_length=254, null=False, blank=False)
    city = models.CharField(
        max_length=100, null=False, blank=False)
    state = models.CharField(
        max_length=100, null=False, blank=False)
    country = models.CharField(
        max_length=100, null=False, blank=False)
    zip = models.PositiveIntegerField(
        null=False, blank=False)

    def __str__(self):
        return self.firstName+" "+self.lastName


class guest(models.Model):
    guestPK = models.AutoField(primary_key=True)
    visitRequestForm = models.ForeignKey(
        visitRequest, on_delete=models.CASCADE, related_name='guests', null=False, blank=False)
    firstName = models.CharField(max_length=50, null=False, blank=False)
    lastName = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False, validators=[
                              EmailValidator(message='Invalid email address')])
    phoneNumber = PhoneNumberField()

    def __str__(self):
        return self.firstName+" "+self.lastName
