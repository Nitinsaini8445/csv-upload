
from django.db import models



class File(models.Model):
    UniqueID= models.IntegerField()
    Company_name= models.CharField(max_length=100 ,null=True ,blank=True)
    Contact_person_Name = models.CharField(max_length=200 ,null=True ,blank=True)
    Contact_phone = models.IntegerField()
    Contact_email= models.CharField(max_length=20 ,null=True ,blank=True)
    
    def __str__(self):
        return self.  Company_name
