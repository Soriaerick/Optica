from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Producto, ServicioReparacion, HorarioAtencion, Categoria, Venta, DetalleVenta


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
# 🔥 SISTEMA DE VENTAS (POS)
# =========================================

@login_required
def realizar_venta(request):
    if request.method == 'POST':
        productos = request.POST.getlist('producto_id')
        cantidades = request.POST.getlist('cantidad')

        # Crear venta
        venta = Venta.objects.create(usuario=request.user)
        total = 0

        for i in range(len(productos)):
            producto = get_object_or_404(Producto, id=productos[i])
            cantidad = int(cantidades[i])

            # ⚠️ Validaciones
            if cantidad <= 0:
                continue

            if producto.stock < cantidad:
                continue

            subtotal = producto.precio * cantidad
            total += subtotal

            # Crear detalle
            DetalleVenta.objects.create(
                venta=venta,
                producto=producto,
                cantidad=cantidad,
                precio=producto.precio
            )

            # 🔥 Descontar stock
            producto.stock -= cantidad
            producto.save()

        venta.total = total
        venta.save()

        return redirect('productos')