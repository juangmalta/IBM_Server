from django.db import models
from user_control.models import CustomUser
# Create your models here.

class Certificaciones(models.Model):
    uid = models.CharField(max_length=100)
    org = models.CharField(max_length=100)
    work_location = models.CharField(max_length=100)
    certifications = models.CharField(max_length=100)
    issue_date = models.DateField()
    type = models.CharField(max_length=100)
    
    
    
    