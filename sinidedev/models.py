from django.db import models

# Create your models here.

class Persona(models.Model):
    nombres = models.CharField(max_length=120)
    apellidos = models.CharField(max_length=120)
    documento = models.IntegerField()

    def __str__(self):
        return self.nombres+" "+self.apellidos