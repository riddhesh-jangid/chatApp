# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class user(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    token = models.AutoField(primary_key=True)

class message(models.Model):
    token = models.ForeignKey(user,on_delete=models.CASCADE)
    text = models.CharField(max_length=100)
    rtoken = models.IntegerField(default=0)

class allconnection(models.Model):
    token = models.ForeignKey(user,on_delete=models.CASCADE)
    ctoken = models.IntegerField(default=0)
