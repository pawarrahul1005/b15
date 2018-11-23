from django.conf.urls import url

from views import *

urlpatterns = [

        url('index/' , index , name='index'),
        url('user/' , add_user , name='user'),
        url('users/' , get_users , name='users'),
        url('devices/' , get_devices , name='devices'),
        ]
