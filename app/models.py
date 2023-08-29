from django.db import models
from django.contrib.auth.models import User
# a los modelos les puse c incialmente para diferenciar las clases en las funciones, ya que en ejercicios anteriores
#se me duplicaron los nombres y no sabía a que hacía referencia.


class cpelicula(models.Model):
    nombre=models.CharField(max_length=50)
    fecha_estreno= models.DateField()
    productora = models.CharField(max_length=50)
    genero = models.CharField(max_length=60)

    class Meta:
        verbose_name ="pelicula"
        verbose_name_plural = "Peliculas"
        ordering = ['nombre']

    def __str__(self):
        return f"{self.nombre}, {self.fecha_estreno}, {self.productora}, {self.genero}"




class cdirector(models.Model):
    nombre = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=50)

    class Meta:
        verbose_name ="director"
        verbose_name_plural = "Directores"
        ordering = ['nombre']
    
    def __str__(self):
        return f"{self.nombre},  {self.nacionalidad}"




class cproductora(models.Model):
    nombre = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)

    class Meta:
        verbose_name ="productora"
        verbose_name_plural = "Productoras"
        ordering = ['nombre']

    def __str__(self):
        return f"{self.nombre}, {self.pais}"

class cAvatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}"