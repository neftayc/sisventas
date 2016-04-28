from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=100, blank=True, default='')
    pat_apellido = models.CharField(max_length=100, blank=True, default='')
    mad_apellido = models.CharField(max_length=100, blank=False, default='')
    dni = models.CharField(max_length=8, blank=True, default='')
    f_nacimiento = models.DateTimeField()
    owner = models.ForeignKey('auth.User', related_name='personas')
    #sexo = models.BooleanField(defaul=False)
    direccion = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Personas"

    def __str__(self):
        return self.nombre
