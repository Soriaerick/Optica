from django.urls import path
from . import views

urlpatterns = [
    # ===== PRINCIPAL =====
    path('', views.inicio, name='inicio'),

    # ===== PRODUCTOS =====
    path('productos/', views.lista_productos, name='productos'),
    path('producto/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),

    # ===== VENTAS =====
    path('venta/', views.realizar_venta, name='venta'),

    # ===== SERVICIOS =====
    path('reparaciones/', views.reparaciones, name='reparaciones'),
    path('horarios/', views.horarios, name='horarios'),

    # ===== CATEGORÍAS =====
    path('categorias/', views.categorias, name='categorias'),
    path('categoria/<int:categoria_id>/', views.productos_por_categoria, name='productos_por_categoria'),

    # ===== REPORTES de VENTAS =====
    path('reporte-ventas/', views.reporte_ventas, name='reporte_ventas'),
]