from django.db import models
from django.contrib.auth.models import User


class Forwarder(models.Model):
    id_forwarder = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ruc = models.CharField(max_length=15)
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=25)
    is_sended_qoutes = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Qoutation(models.Model):
    id_qoutation = models.AutoField(primary_key=True)
    forwarder = models.ForeignKey(Forwarder, on_delete=models.CASCADE)
    country = models.CharField(max_length=255)
    supplier = models.CharField(max_length=255)
    incoterm = models.CharField(max_length=25)
    portOrigin = models.CharField(max_length=55)
    portDestination = models.CharField(max_length=55)
    transitDays = models.IntegerField(default=0)
    gOrigin = models.FloatField(default=0)
    freight = models.FloatField(default=0)
    localExpenses = models.FloatField(default=0)
    freeDays = models.IntegerField(default=0)
    offerDays = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.supplier.name
