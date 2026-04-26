# admin.py
from django.contrib import admin
from .models import SystemInfo, Schedule

admin.site.register(SystemInfo)
admin.site.register(Schedule)