from django.db import models

# Create your models here.

#Familia
class Familia(models.Model):

    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    nacimiento = models.DateField()

    def __str__(self):
        return self.nombre
