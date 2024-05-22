from django.db import models

# Create your models here.
class employee(models.Model):
    eid = models.IntegerField(primary_key=True)
    eage = models.IntegerField()
    ename = models.CharField(max_length=20)
    esalary = models.IntegerField()