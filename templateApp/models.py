from django.db import models

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=100)
    no_people=models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    day_of_week = models.CharField(max_length=100)
