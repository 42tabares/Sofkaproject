from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Company(models.Model):
    manager     = models.ForeignKey(User, on_delete=models.CASCADE)
    name        = models.CharField(max_length=50)
    description = models.CharField(max_length=2000, default="", blank=True)
    logo        = models.CharField(max_length=300, default="", blank=True)


class Hotel(models.Model):
    company     = models.ForeignKey(Company, default="None", on_delete=models.CASCADE)
    name        = models.CharField(max_length=50)
    location    = models.CharField(max_length=50, default = "unknown")
    description = models.CharField(max_length=2000, default="", blank=True)
    image       = models.CharField(max_length=300, default="", blank=True)
    

class RoomType(models.Model):
    hotel       = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    category    = models.CharField(max_length=50, null=True, blank=True)
    description = models.CharField(max_length=300, null=True, blank=True)
    image       = models.CharField(max_length=300, default="", blank=True)
    cost        = models.FloatField(max_length=50, default = 0)


class Reservation(models.Model):

    company     = models.CharField(max_length=50)
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel_name  = models.CharField(max_length=50)
    roomtype    = models.CharField(max_length=50)
    customer    = models.CharField(max_length=100, null=False, blank=False)
    customer_email=models.CharField(max_length=100,null=False, blank=False)
    customer_fn = models.CharField(max_length=100)
    customer_ln = models.CharField(max_length=100)
    status      = models.BooleanField(blank=True, null=True, default=None)
    date_start  = models.DateField(null=False, blank=False)
    date_end    = models.DateField(null=False, blank=False)
    date_created= models.DateTimeField(default="Unknown")
    date_update = models.DateTimeField(default=None)


