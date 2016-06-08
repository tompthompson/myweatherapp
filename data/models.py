from django.db import models
from django.utils import timezone

# Create your models here.
class Weather(models.Model):
    location = models.CharField(max_length=50)
    temp_today = models.IntegerField()
    temp_tomorrow = models.IntegerField()

class UserInfo(models.Model):
    user = models.ForeignKey('auth.User')
    name = models.CharField(max_length=50)
    location = models.ForeignKey(Weather)
    alert_temp = models.IntegerField(default=15)
