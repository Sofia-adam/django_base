from django.db import models

# Create your models here.
class owner(models.Model):
    oname = models.CharField(max_length=20)
    oadd = models.CharField(max_length=20)
    def __str__(self):
        return "%s %s"%(self.oname,self.oadd)
    
class car(models.Model):
    cbrand = models.CharField(max_length=10)
    cmodel = models.CharField(max_length=10)
    ctype = models.CharField(max_length=10)
    owner = models.ForeignKey(owner,on_delete=models.CASCADE)
    def __str__(self):
        return "%s %s %s %s"%(self.cbrand,self.cmodel,self.ctype,self.owner)