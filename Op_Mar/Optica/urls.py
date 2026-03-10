from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('productos/', views.lista_productos, name='productos'), 
    path('reparaciones/', views.reparaciones, name='reparaciones'),
    path('horarios/', views.horarios, name='horarios'),
    path('producto/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
]