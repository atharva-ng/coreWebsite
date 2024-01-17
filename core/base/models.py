from django.db import models
# from django.utils import timezone
# Create your models here.


class contactDetail(models.Model):
    sno = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=50, default="defaultName")
    lastName = models.CharField(max_length=50, default="defaultName")
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=254)
    message = models.TextField(max_length=508)
    contacted = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.firstName+' '+self.lastName


# class person(models.Model):
#     name = models.TextField(max_length=100)
#     linkdn = models.TextField(max_length=100)
#     photo = models.ImageField()

#     def __str__(self):
#         return self.name


# class coordi(models.Model):
#     personDetails = models.ForeignKey(
#         person, on_delete=models.CASCADE, related_name="coordi")
#     position = models.TextField(max_length=100)

#     def __str__(self):
#         return self.position


class blog(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="blogImages/")
    link = models.URLField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
