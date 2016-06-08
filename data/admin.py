from django.contrib import admin
from .models import Weather
from .models import UserInfo
# Register your models here.

admin.site.register(Weather)
admin.site.register(UserInfo)
