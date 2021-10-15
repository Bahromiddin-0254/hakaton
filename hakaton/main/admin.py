from django.contrib import admin
from django.apps import apps
from .models import *
# Register your models here.
apps.get_app_config('admin').module.site.register(Lesson)