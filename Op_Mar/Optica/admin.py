from django.contrib import admin
from .models import Categoria, Producto, ServicioReparacion, HorarioAtencion
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'precio', 'categoria', 'stock', 'destacado']
    list_filter = ['categoria', 'destacado']
    search_fields = ['nombre']

@admin.register(ServicioReparacion)
class ServicioReparacionAdmin(admin.ModelAdmin):
    list_display = ['tipo_reparacion', 'precio_estimado', 'tiempo_estimado']

@admin.register(HorarioAtencion)
class HorarioAtencionAdmin(admin.ModelAdmin):
    list_display = ['dia_semana', 'horario_apertura', 'horario_cierre']

admin.site.register(Categoria)