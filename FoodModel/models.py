from django.db import models

# Create your models here.
class Food(models.Model):
    foodname = models.CharField(max_length=30)
