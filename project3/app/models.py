from django.db import models

# Create your models here.
class departments(models.Model):
    dname=models.TextField()
    
    def _str_(self):
        return self.dname
class employee(models.Model):
    name=models.TextField()
    email=models.TextField()
    username=models.TextField()
    password=models.TextField()
    dname=models.ForeignKey(departments,on_delete=models.CASCADE)

    
    def _str_(self):
        return self.name
    