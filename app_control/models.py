from django.db import models
from user_control.models import CustomUser
# Create your models here.

class Certificaciones(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    