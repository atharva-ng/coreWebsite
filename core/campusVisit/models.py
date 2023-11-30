from django.db import models

# Create your models here.


class campusVisitRequest(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    studentId = models.CharField(max_length=13)
    email = models.EmailField(max_length=254)
    phoneNumber = models.IntegerField()
    reason = models.CharField(max_length=254)
    datesFrom = models.DateField(verbose_name="From Date")
    datesTo = models.DateField(verbose_name="To Date")
