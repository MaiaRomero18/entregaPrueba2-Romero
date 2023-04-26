from django.db import models
from django.contrib.auth.models import User

class Alumnos(models.Model):
    nombre= models.CharField(max_length=100)
    apellido= models.CharField(max_length=100)
    mail= models.CharField(max_length=280)
    nivel= models.CharField(max_length=100)
    contrasena1= models.CharField(max_length=150)
    contrasena2= models.CharField(max_length=150)
    
class Profesor(models.Model):
    nombre= models.CharField(max_length=100)
    apellido= models.CharField(max_length=100)
    mail= models.CharField(max_length=280)
    contrasena1= models.CharField(max_length=150)
    contrasena2= models.CharField(max_length=150)
