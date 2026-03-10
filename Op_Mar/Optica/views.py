from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, ServicioReparacion, HorarioAtencion, Categoria

# Create your views here.

def inicio(request):
    productos_destacados = Producto.objects.filter(destacado=True)[:6]
    return render(request, 'optica/inicio.html', {
        'productos_destacados': productos_destacados
    })

def lista_productos(request):
    categoria_seleccionada = request.GET.get('categoria')
    
    if categoria_seleccionada:
        productos = Producto.objects.filter(categoria__nombre=categoria_seleccionada)
    else:
        productos = Producto.objects.all()
    
    categorias = Categoria.objects.all()
    
    return render(request, 'optica/productos.html', {
        'productos': productos,
        'categorias': categorias,
        'categoria_seleccionada': categoria_seleccionada
    })

def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, 'optica/detalle_producto.html', {
        'producto': producto
    })

def reparaciones(request):
    servicios = ServicioReparacion.objects.all()
    return render(request, 'optica/reparaciones.html', {
        'servicios': servicios
    })

def horarios(request):
    horarios_atencion = HorarioAtencion.objects.all()
    return render(request, 'optica/horarios.html', {
        'horarios': horarios_atencion
    })
def agendar_cita(request):
    
    return render(request, 'optica/agendar_cita.html')