from django.db import models
from django.contrib.auth.models import User

class SystemInfo(models.Model):
    water_level = models.CharField(max_length=50)
    tank_status = models.CharField(max_length=50)

    def __str__(self):
        return f"Water Level: {self.water_level}, Tank: {self.tank_status}"

class Schedule(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    irrigation_days = models.IntegerField()
    times_per_day = models.IntegerField()

    def __str__(self):
        return f"{self.user.username} - {self.date}"