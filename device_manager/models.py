# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    u_id = models.CharField(primary_key=True,max_length = 10)
    u_name = models.CharField(max_length = 100)
    u_gender = models.CharField(max_length=1)
    u_mob = models.CharField(max_length = 15)
    u_email = models.CharField(max_length = 100)

    def __eq__(self , other_user):
        if self.u_id == other_user.u_id:
            return True
        return False

    def __str__(self):
        return "CT-id : "+u_id+"  Name : "+u_name

    def __repr__(self):
        return "CT-id : "+u_id+"  Name : "+u_name

class Device(models.Model):
    d_id = models.IntegerField(primary_key=True)
    d_name = models.CharField(max_length = 32)
    d_state = models.CharField(max_length = 5)#current state of the device

class User_Device(models.Model):
    u = models.ForeignKey(User)
    d = models.ForeignKey(Device)
