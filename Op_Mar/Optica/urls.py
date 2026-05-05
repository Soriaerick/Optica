from django.urls import path
from . import views

urlpatterns = [
    # Rutas para la página de inicio
    path('', views.inicio, name='inicio'),

    # Rutas para productos
    path('productos/', views.lista_productos, name='productos'),
    path('producto/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),

    # Rutas para ventas
    path('venta/', views.realizar_venta, name='venta'),

    # Rutas para servicios de reparación
    path('reparaciones/', views.reparaciones, name='reparaciones'),
    path('horarios/', views.horarios, name='horarios'),

    # Rutas para categorías
    path('categorias/', views.categorias, name='categorias'),
    path('categoria/<int:categoria_id>/', views.productos_por_categoria, name='productos_por_categoria'),

    # Rutas para reportes
    path('reporte-ventas/', views.reporte_ventas, name='reporte_ventas'),

    # Rutas para el carrito de compras
    path('carrito/', views.ver_carrito, name='carrito'),
    path('carrito/agregar/<int:producto_id>/', views.agregar_carrito, name='agregar_carrito'),
    path('carrito/eliminar/<int:producto_id>/', views.eliminar_carrito, name='eliminar_carrito'),
    path('carrito/confirmar/', views.confirmar_compra, name='confirmar_compra'),

    # Ruta para agendar citas
    path('agendar-cita/', views.agendar_cita, name='agendar_cita'),
]