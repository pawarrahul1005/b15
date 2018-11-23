# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt,ensure_csrf_cookie
from django_tables2 import RequestConfig
from forms import *
from models import *
# Create your views here.

users_list = []
devices_list = []



def index(request):
    template = loader.get_template("device_manager/users.html")
    form = UserForm()
    context = {'form' : form}
    return HttpResponse(template.render(context , request))

@csrf_exempt
def add_user(request):
    user_form = UserForm(request.POST)
    if user_form.is_valid():
        print user_form.cleaned_data
    data = user_form.cleaned_data
    user = User(u_id = data['ct_id'] , u_name = data['name'] , u_email = data['email'] , u_gender = data['gender'] , u_mob = data['mob'])
    try:
        user.save()
        users_list.append(user)
    except:
        pass
    return HttpResponse("add user me aaya")

def delete_user():
    pass

def update_user():
    pass


def get_users(request):
    template = loader.get_template("device_manager/users.html")
    users = User.objects.all()
    form = UserForm()
    context = {'form':form,'users' : users}
    return HttpResponse(template.render(context , request))


def add_device(request):
    device_form = DeviceForm(request.POST)
    if deivce_form.is_valid():
        print device_form.cleaned_data
    data = device_form.cleaned_data
    device = Device(d_id = data['device_id'] , d_name = data['name'] , d_state = data['state'])
    try:
        device.save()
        devices_list.append(user)
    except:
        pass
    return HttpResponse("add device me aaya")


def get_devices(request):
    template = loader.get_template("device_manager/devices.html")
    devices = Device.objects.all()
    form_device = DeviceForm()
    context = {'devices' : devices , 'form':form_device}
    return HttpResponse(template.render(context , request))
