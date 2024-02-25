from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# from django.db.models.signals import post_save
# from django.dispatch import receiver


class contactDetail(models.Model):
    sno = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=50, default="defaultName")
    lastName = models.CharField(max_length=50, default="defaultName")
    email = models.EmailField(max_length=254)
    phoneNumber = PhoneNumberField()
    subject = models.CharField(max_length=254)
    message = models.TextField(max_length=508)
    contacted = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.contacted:
            response = "Contacted"
        else:
            response = "Not Contacted"
        return self.firstName+' '+self.lastName + ' '+response


# @receiver(post_save, sender=contactDetail)
# def print_hello_on_first_save(sender, instance, created, **kwargs):
#     if created:
#         print("==================================Hello==================================================")


# post_save.connect(print_hello_on_first_save, sender=contactDetail)


class blog(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="blogImages/")
    link = models.URLField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class event(models.Model):
    title = models.CharField(max_length=254, null=False, blank=False)
    image = models.ImageField(upload_to="eventsImages/")
    content = models.CharField(max_length=1016, null=False, blank=False)
    created = models.DateField()
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
