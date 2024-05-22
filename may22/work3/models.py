from django.db import models

# Create your models here.
class showroom(models.Model):
    sname = models.CharField(max_length=30)
    sloc = models.CharField(max_length=30)
    def __str__(self):
        return "%s %s"%(self.sname,self.sloc)
    
class car(models.Model):
    cbrand = models.CharField(max_length=20)
    cmodel = models.CharField(max_length=20)
    ctype = models.CharField(max_length=20)
    showroom = models.ManyToManyField(showroom)
    def __str__(self):
        return "%s %s %s"%(self.cbrand,self.cmodel,self.ctype)