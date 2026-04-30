from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Producto, ServicioReparacion, HorarioAtencion, Categoria, Venta, DetalleVenta
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from datetime import datetime


# ===== INICIO =====
def inicio(request):
    productos_destacados = Producto.objects.filter(destacado=True)[:6]
    return render(request, 'optica/inicio.html', {
        'productos_destacados': productos_destacados
    })


# ===== PRODUCTOS =====
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


# ===== DETALLE =====
def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, 'optica/detalle_producto.html', {
        'producto': producto
    })


# ===== REPARACIONES =====
def reparaciones(request):
    servicios = ServicioReparacion.objects.all()
    return render(request, 'optica/reparaciones.html', {
        'servicios': servicios
    })


# ===== HORARIOS =====
def horarios(request):
    horarios_atencion = HorarioAtencion.objects.all()
    return render(request, 'optica/horarios.html', {
        'horarios': horarios_atencion
    })


# ===== AGENDAR CITA =====
def agendar_cita(request):
    return render(request, 'optica/agendar_cita.html')


# =========================================
#  SISTEMA DE VENTAS    
# =========================================
@login_required
def realizar_venta(request):
    if request.method != 'POST':
        return redirect('productos')  # evita acceso directo

    productos_ids = request.POST.getlist('productos')

    if not productos_ids:
        return redirect('productos')

    venta = Venta.objects.create(usuario=request.user)
    total = 0

    for producto_id in productos_ids:
        producto = get_object_or_404(Producto, id=producto_id)

        cantidad = int(request.POST.get(f'cantidad_{producto_id}', 1))

        if cantidad <= 0:
            continue

        if producto.stock < cantidad:
            continue

        subtotal = producto.precio * cantidad
        total += subtotal

        DetalleVenta.objects.create(
            venta=venta,
            producto=producto,
            cantidad=cantidad,
            precio=producto.precio
        )

        # descontar stock
        producto.stock -= cantidad
        producto.save()

    # evitar guardar venta vacía
    if total == 0:
        venta.delete()
        return redirect('productos')

    venta.total = total
    venta.save()

    return redirect('productos')


# =========================================
#  CATEGORÍAS
# =========================================
def productos_por_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    productos = Producto.objects.filter(categoria=categoria)

    return render(request, 'optica/productos_categoria.html', {
        'categoria': categoria,
        'productos': productos
    })


def categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'optica/categorias.html', {
        'categorias': categorias
    })


# ========================================= 
#  REPORTES DE VENTAS
# =========================================
@login_required
def reporte_ventas(request):
    ventas = Venta.objects.all().order_by('-fecha')

    fecha_inicio = request.GET.get('inicio')
    fecha_fin = request.GET.get('fin')

    # FILTRO POR FECHA
    if fecha_inicio and fecha_fin:
        ventas = ventas.filter(fecha__date__range=[fecha_inicio, fecha_fin])

    total_vendido = ventas.aggregate(total=Sum('total'))['total'] or 0

    return render(request, 'optica/reporte_ventas.html', {
        'ventas': ventas,
        'total_vendido': total_vendido,
        'fecha_inicio': fecha_inicio,
        'fecha_fin': fecha_fin
    })