from django.db import models


# Create your models here.

class Userinfo(models.Model):

    name                    = models.CharField(max_length=100)
    blood_group             = models.CharField(max_length=10)
    phone_number            = models.TextField(max_length=10)
    place                    = models.CharField(max_length=50)



