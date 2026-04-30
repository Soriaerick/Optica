from django.db import models
from django.contrib.auth.models import User


# ===== CATEGORIA =====
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


# ===== SUBCATEGORIA (FALTABA) =====
class SubCategoria(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} ({self.categoria.nombre})"


# ===== PRODUCTO =====
class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    subcategoria = models.ForeignKey(SubCategoria, on_delete=models.CASCADE, null=True, blank=True)

    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)
    stock = models.IntegerField(default=0)
    destacado = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre

    def hay_stock(self, cantidad):
        return self.stock >= cantidad


# ===== SERVICIOS =====
class ServicioReparacion(models.Model):
    tipo_reparacion = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio_estimado = models.DecimalField(max_digits=10, decimal_places=2)
    tiempo_estimado = models.CharField(max_length=50)

    def __str__(self):
        return self.tipo_reparacion


# ===== PACIENTES =====
class Datos_paciente(models.Model):
    nombre_cliente = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    fecha = models.DateField()
    servicio = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nombre_cliente} - {self.fecha}'


# ===== HORARIOS =====
class HorarioAtencion(models.Model):
    dia_semana = models.CharField(max_length=20)
    horario_apertura = models.TimeField()
    horario_cierre = models.TimeField()

    def __str__(self):
        return f"{self.dia_semana}: {self.horario_apertura} - {self.horario_cierre}"


# ===== VENTAS =====
class Venta(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def calcular_total(self):
        total = sum(detalle.subtotal() for detalle in self.detalles.all())
        self.total = total
        self.save()

    def __str__(self):
        return f"Venta #{self.id} - {self.usuario.username}"


class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def subtotal(self):
        return self.precio * self.cantidad

    def __str__(self):
        return f"{self.producto.nombre} x {self.cantidad}"