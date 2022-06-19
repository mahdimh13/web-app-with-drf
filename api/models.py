from django.db import models
from datetime import datetime

# Create your models here.

class Item(models.Model):
    key=models.CharField(max_length=100,primary_key=True)
    value=models.TextField()
    time=models.TimeField(default=datetime.now().strftime("%H:%M:%S"))
    def __str__(self):
        return self.key


class History(models.Model):
    key = models.CharField(max_length=100)
    value = models.TextField()
    time = models.TimeField(default=datetime.now().strftime("%H:%M:%S"))
    def __str__(self):
        return self.key