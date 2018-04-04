# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Owner(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    	

class Pet(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    birthday = models.DateField()
    PET_CHOICES = (
        ('D', 'Dog'),
        ('C', 'Cat'),
    )
    pet_type= models.CharField(max_length=1, choices=PET_CHOICES)
    def __str__(self):
        return self.name

# Create your models here.
