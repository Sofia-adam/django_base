from django.db import models

# Create your models here.
class car(models.Model):
    cbrand = models.CharField(max_length=20)
    cmodel = models.CharField(max_length=20)
    ctype = models.CharField(max_length=10)
    def __str__(self):
        return "car brand:%s car model:%s car type:%s"%(self.cbrand,self.cmodel,self.ctype)
    
class driver(models.Model):
    dname = models.CharField(max_length=20)
    dadd = models.CharField(max_length=20)
    car = models.OneToOneField(car,on_delete=models.CASCADE)
    def __str__(self):
        return "driver name:%s driver address:%s car details:%s"%(self.dname, self.dadd, self.car)