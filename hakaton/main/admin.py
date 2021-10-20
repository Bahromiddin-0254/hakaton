from django.contrib import admin
from django.apps import apps
from .models import *
# Register your models here.

for i in apps.get_app_config('main').models:    
    apps.get_app_config('admin').module.site.register(apps.get_app_config('main').models[i])