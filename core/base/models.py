from django.db import models

# Create your models here.


class cordi(models.Model):
    name = models.TextField()
    linkdn = models.TextField()
    photo = models.ImageField()
    intro = models.CharField(max_length=300)
