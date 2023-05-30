from django.db import models
from user_control.models import CustomUser
# Create your models here.

class Certificaciones(models.Model):
    uid = models.CharField(max_length=500)
    org = models.CharField(max_length=500)
    work_location = models.CharField(max_length=500,null=True,blank=True)
    certifications = models.CharField(max_length=500)
    issue_date = models.DateField(null=True, blank=True)
    type = models.CharField(max_length=500)
    
    
    
    