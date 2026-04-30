from django.contrib import admin
from .models import Categoria, SubCategoria, Producto, ServicioReparacion, HorarioAtencion, Datos_paciente


@admin.register(SubCategoria)
class SubCategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'categoria']
    list_filter = ['categoria']
    search_fields = ['nombre']


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'precio', 'categoria', 'subcategoria', 'stock', 'destacado']
    list_filter = ['categoria', 'subcategoria', 'destacado']
    search_fields = ['nombre']


@admin.register(ServicioReparacion)
class ServicioReparacionAdmin(admin.ModelAdmin):
    list_display = ['tipo_reparacion', 'precio_estimado', 'tiempo_estimado']


@admin.register(HorarioAtencion)
class HorarioAtencionAdmin(admin.ModelAdmin):
    list_display = ['dia_semana', 'horario_apertura', 'horario_cierre']


@admin.register(Datos_paciente)
class DatosPacienteAdmin(admin.ModelAdmin):
    list_display = ['nombre_cliente', 'telefono', 'fecha', 'servicio']


admin.site.register(Categoria)