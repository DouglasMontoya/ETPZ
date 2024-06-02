
from django.db import models

class PeriodosAcademicos(models.Model):
    id = models.AutoField(primary_key=True)  # Llave primaria autoincremental
    nombre = models.CharField(max_length=255, null=False)  # String de 255 de longitud

    def __str__(self):
        return self.nombre  # Representación en cadena del objeto

    class Meta:
        verbose_name_plural = "Periodos Académicos"  # Nombre en plural para el panel de administración


class DatosPlantel(models.Model):
    id = models.AutoField(primary_key=True)  # Llave primaria autoincremental
    codigo = models.CharField(max_length=255)  # Cadena de texto no nula
    nombre = models.CharField(max_length=255)  # Cadena de texto no nula
    direccion = models.CharField(max_length=255)  # Cadena de texto no nula
    telefono = models.PositiveIntegerField()  # Número no nulo
    municipio = models.CharField(max_length=255)  # Cadena de texto no nula
    entidad_federal = models.CharField(max_length=255)  # Cadena de texto no nula
    zona_educativa = models.CharField(max_length=255)  # Cadena de texto no nula
    distrito_escolar = models.CharField(max_length=255)  # Cadena de texto no nula
    ci_tipo = models.CharField(max_length=1, null=False)  # String de un solo carácter no nulo
    ci = models.PositiveIntegerField(null=False)  # Número no nulo
    director = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre  # Representación en cadena del objeto

    class Meta:
        verbose_name_plural = "Datos Plantel"  # Nombre en plural para el panel de administración

class Estudiantes(models.Model):
    id = models.AutoField(primary_key=True)  # Llave primaria autoincremental
    ci_tipo = models.CharField(max_length=1, null=False)  # String de un solo carácter no nulo
    ci = models.PositiveIntegerField(null=False)  # Número no nulo
    nombres = models.CharField(max_length=255)  # Cadena de texto no nula
    apellidos = models.CharField(max_length=255)  # Cadena de texto no nula
    sexo = models.CharField(max_length=255)
    fecha_de_nacimiento = models.DateField(auto_now=True, auto_now_add=False)
    anio = models.CharField(max_length=255)
    mencion = models.CharField(max_length=5, null=False)  # String de cinco caracteres no nulo
    seccion = models.CharField(max_length=1, null=False)  # String de un solo carácter no nulo
    entidad_federal = models.CharField(max_length=255)  # Cadena de texto no nula
    lugar_de_nacimiento = models.CharField(max_length=255)  # Cadena de texto no nula
    
    def __str__(self):
        return self.nombre  # Representación en cadena del objeto
    
    class Meta:
        verbose_name_plural = "Estudiantes"  # Nombre en plural para el panel de administración

class Anios(models.Model):
    id = models.AutoField(primary_key=True)  # Llave primaria autoincremental
    nombre = models.CharField(max_length=255, null=False)  # Cadena de texto no nula

    def __str__(self):
        return self.nombre  # Representación en cadena del objeto

    class Meta:
        verbose_name_plural = "Años"  # Nombre en plural para el panel de administración

class Menciones(models.Model):
    id = models.AutoField(primary_key=True)  # Llave primaria autoincremental
    nombre = models.CharField(max_length=255, null=False, unique=True)  # String de 255 de longitud
    nombre_abrev = models.CharField(max_length=5, null=False, unique=True)  # String de 255 de longitud

    def __str__(self):
        return self.nombre  # Representación en cadena del objeto

    class Meta:
        verbose_name_plural = "Menciones"  # Nombre en plural para el panel de administración

class Secciones(models.Model):
    id = models.AutoField(primary_key=True)  # Llave primaria autoincremental
    nombre = models.CharField(max_length=3, null=False, unique=True)  # String de 255 de longitud

    def __str__(self):
        return self.nombre  # Representación en cadena del objeto

    class Meta:
        verbose_name_plural = "Secciones"  # Nombre en plural para el panel de administración

class AniosMencionSec(models.Model):
    anio = models.ForeignKey(Anios, on_delete=models.CASCADE)
    mencion = models.ForeignKey(Menciones, on_delete=models.CASCADE)
    seccion= models.ForeignKey(Secciones, on_delete=models.CASCADE)

    def __str__(self):
        return f'{ self.anio.nombre } - { self.mencion.nombre } - { self.seccion.nombre }'  # Representación en cadena del objeto

    class Meta:
        verbose_name_plural = "Años Menciones Secciones"
        constraints = [
            models.UniqueConstraint(fields=['anio', 'mencion', 'seccion'], name='unique_anio_mencion_seccion')
        ]