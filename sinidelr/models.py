from django.db import models

# Create your models here.


class Persona(models.Model):

    id_persona = models.AutoField(primary_key=True)

    nombres = models.CharField(max_length=120,help_text='Ingresar el NOMBRE para el legajo del alumno')

    apellidos = models.CharField(max_length=120,help_text='Ingresar el APELLIDO para el legajo del alumno')

    documento = models.IntegerField(help_text='Ingresar el DOCUMENTO para el legajo del alumno')

    cuit = models.CharField(max_length=13, help_text='Ingresar el CUIT para el legajo del alumno')

    fecha_nacimiento = models.DateField(help_text='Ingresar la FECHA DE NAC para el legajo del alumno')

    lugar_nacimiento = models.CharField(max_length=60)

    email = models.EmailField();

    codigo_area_telefono = models.CharField(max_length=15)

    numero_telefono = models.CharField(max_length=15)


    def __str__(self):
        return self.nombres


class Direccion(models.Model):

    id_direccion = models.AutoField(primary_key=True)

    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)

    calle = models.CharField(max_length=120)

    barrio = models.CharField(max_length=120)

    numero = models.IntegerField();



