from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='productos/')
    stock = models.IntegerField(default=0)
    destacado = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre
    
class ServicioReparacion(models.Model):
    tipo_reparacion = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio_estimado = models.DecimalField(max_digits=10, decimal_places=2)
    tiempo_estimado = models.CharField(max_length=50)
    
    def __str__(self):
        return self.tipo_reparacion    

class Datos_paciente(models.Model):
    nombre_cliente = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    fecha = models.DateField()
    servicio = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nombre_cliente} - {self.fecha}'

class HorarioAtencion(models.Model):
    dia_semana = models.CharField(max_length=20)
    horario_apertura = models.TimeField()
    horario_cierre = models.TimeField()
    
    def __str__(self):
        return f"{self.dia_semana}: {self.horario_apertura} - {self.horario_cierre}"