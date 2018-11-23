# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms

# Create your forms here.
class UserForm(forms.Form):
    choices = [("d1" , "device1"),("d2","device2")]
    ct_id = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'CT-id'}),max_length = 10)
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'name'}),max_length = 100)
    gender = forms.CharField(widget=forms.Select(choices=[('M',"Male"),('F',"Female"),('O',"other")],attrs={'class':'form-control','placeholder':'M/F'}),max_length=1)
    mob = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'mobile number'}),max_length = 15)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'email'}),max_length = 100)
    permissions = forms.MultipleChoiceField(required=False,widget=forms.CheckboxSelectMultiple,choices=choices)
    
   # def is_valid(self):
   #     super(forms.Form , self).is_valid()
   #     print self.cleaned_data
   #     cleaned_data = self.cleaned_data
   #     self.u_id.clean(cleaned_data['u_id'])
   #     self.u_name.clean(cleaned_data['u_name'])
   #     self.u_gender.clean(cleaned_data['u_gender'])
   #     self.u_mob.clean(cleaned_data['u_mob'])
   #     self.u_email.clean(cleaned_data['u_email'])
class DeviceForm(forms.Form):
    device_id = forms.IntegerField()
    name = forms.CharField(max_length = 32)
    state = forms.CharField(max_length = 5)#current state of the device

