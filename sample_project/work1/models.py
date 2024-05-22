from django.db import models

# Create your models here.
class table1(models.Model):
    name = models.CharField(max_length=20)
    place = models.CharField(max_length=15)
    age = models.IntegerField()
    email = models.EmailField(max_length=20)