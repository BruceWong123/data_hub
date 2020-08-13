# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Bag(models.Model):
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    uploader = models.CharField(max_length=20)
    vehicle = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20)
    start = models.CharField(max_length=30, default='0')
    end = models.CharField(max_length=30, default='0')
    bagid = models.CharField(max_length=30, default="   ", unique=True)

    def __str__(self):
        return self.first_name
