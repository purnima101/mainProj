from ctypes import addressof
from pydoc import describe
from django.db import models

# Create your models here.

class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phn=models.CharField(max_length=100)
    desc=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    # posted=models.BooleanField()

    def __str__(self):
        return self.name


class Sigin(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phn=models.CharField(max_length=100)
    desc=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    # posted=models.BooleanField()

    def __str__(self):
        return self.name