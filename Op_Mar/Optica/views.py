from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from datetime import datetime
from django.contrib import messages

from .models import (
    Producto,
    ServicioReparacion,
    HorarioAtencion,
    Categoria,
    Venta,
    DetalleVenta,
    Cita
)


# =========================================
# INICIO
# =========================================
def inicio(request):
    productos_destacados = Producto.objects.filter(destacado=True)[:6]
    return render(request, 'optica/inicio.html', {
        'productos_destacados': productos_destacados
    })


# =========================================
# PRODUCTOS
# =========================================
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


# =========================================
# CATEGORÍAS
# =========================================
def categorias(request):
    categorias = Categoria.objects.all()

    return render(request, 'optica/categorias.html', {
        'categorias': categorias
    })


def productos_por_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    productos = Producto.objects.filter(categoria=categoria)

    return render(request, 'optica/productos_categoria.html', {
        'categoria': categoria,
        'productos': productos
    })


# =========================================
# REPARACIONES
# =========================================
def reparaciones(request):
    servicios = ServicioReparacion.objects.all()

    return render(request, 'optica/reparaciones.html', {
        'servicios': servicios
    })


# =========================================
# HORARIOS
# =========================================
def horarios(request):
    horarios_atencion = HorarioAtencion.objects.all()

    return render(request, 'optica/horarios.html', {
        'horarios': horarios_atencion
    })


# =========================================
# CARRITO
# =========================================
def agregar_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)

    carrito = request.session.get('carrito', {})

    if str(producto_id) in carrito:
        carrito[str(producto_id)]['cantidad'] += 1
    else:
        carrito[str(producto_id)] = {
            'nombre': producto.nombre,
            'precio': float(producto.precio),
            'cantidad': 1
        }

    request.session['carrito'] = carrito

    return redirect('carrito')


def ver_carrito(request):
    carrito = request.session.get('carrito', {})

    carrito_limpio = {}
    total = 0

    for producto_id, item in carrito.items():
        if not isinstance(item, dict):
            continue

        precio = float(item.get('precio', 0))
        cantidad = int(item.get('cantidad', 0))
        subtotal = precio * cantidad

        carrito_limpio[producto_id] = {
            'nombre': item.get('nombre', 'Producto'),
            'precio': precio,
            'cantidad': cantidad,
            'subtotal': subtotal
        }

        total += subtotal

    request.session['carrito'] = carrito_limpio

    return render(request, 'optica/carrito.html', {
        'carrito': carrito_limpio,
        'total': total
    })


def eliminar_carrito(request, producto_id):
    carrito = request.session.get('carrito', {})

    if str(producto_id) in carrito:
        del carrito[str(producto_id)]

    request.session['carrito'] = carrito

    return redirect('carrito')


@login_required
def confirmar_compra(request):
    carrito = request.session.get('carrito', {})

    if not carrito:
        return redirect('productos')

    venta = Venta.objects.create(usuario=request.user)
    total = 0

    for producto_id, item in carrito.items():
        producto = get_object_or_404(Producto, id=producto_id)

        cantidad = item['cantidad']

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

        producto.stock -= cantidad
        producto.save()

    venta.total = total
    venta.save()

    request.session['carrito'] = {}

    return redirect('productos')


# =========================================
# VENTA DIRECTA
# =========================================
@login_required
def realizar_venta(request):
    if request.method != 'POST':
        return redirect('productos')

    productos_ids = request.POST.getlist('productos')

    if not productos_ids:
        return redirect('productos')

    venta = Venta.objects.create(usuario=request.user)
    total = 0

    for producto_id in productos_ids:
        producto = get_object_or_404(Producto, id=producto_id)

        cantidad = int(request.POST.get(f'cantidad_{producto_id}', 1))

        if cantidad <= 0 or producto.stock < cantidad:
            continue

        subtotal = producto.precio * cantidad
        total += subtotal

        DetalleVenta.objects.create(
            venta=venta,
            producto=producto,
            cantidad=cantidad,
            precio=producto.precio
        )

        producto.stock -= cantidad
        producto.save()

    if total == 0:
        venta.delete()
        return redirect('productos')

    venta.total = total
    venta.save()

    return redirect('productos')


# =========================================
# REPORTE DE VENTAS
# =========================================
@login_required
def reporte_ventas(request):
    # --- Lógica de Ventas ---
    ventas = Venta.objects.all().prefetch_related('detalles__producto').order_by('-fecha')
    
    # --- Lógica de Citas ---
    citas = Cita.objects.all().order_by('-fecha', '-hora')

    fecha_inicio = request.GET.get('inicio')
    fecha_fin = request.GET.get('fin')

    if fecha_inicio and fecha_fin:
        ventas = ventas.filter(fecha__date__range=[fecha_inicio, fecha_fin])
        citas = citas.filter(fecha__range=[fecha_inicio, fecha_fin]) # Filtramos citas también

    total_vendido = ventas.aggregate(total=Sum('total'))['total'] or 0

    return render(request, 'optica/reporte_ventas.html', {
        'ventas': ventas,
        'citas': citas,  # <-- Enviamos las citas al HTML
        'total_vendido': total_vendido,
        'fecha_inicio': fecha_inicio,
        'fecha_fin': fecha_fin
    })

# =========================================
# AGENDAR CITA CON VALIDACIÓN DE HORARIO
# =========================================
def agendar_cita(request):
    # Traemos los horarios para mostrarlos en la página
    horarios_disponibles = HorarioAtencion.objects.all()

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        telefono = request.POST.get('telefono')
        fecha_str = request.POST.get('fecha')
        hora_str = request.POST.get('hora')
        motivo = request.POST.get('motivo')

        # 1. Convertimos el texto a formato de fecha y hora de Python
        try:
            fecha_obj = datetime.strptime(fecha_str, '%Y-%m-%d').date()
            hora_obj = datetime.strptime(hora_str, '%H:%M').time()
        except ValueError:
            messages.error(request, "Hubo un error con el formato de la fecha.")
            return redirect('agendar_cita')

        # 2. Saber qué día de la semana es (0=Lunes, 6=Domingo)
        dias_espanol = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
        dia_semana_elegido = dias_espanol[fecha_obj.weekday()]

        # 3. Buscar si la óptica abre ese día (usamos icontains para evitar problemas con mayúsculas)
        horario_dia = HorarioAtencion.objects.filter(dia_semana__icontains=dia_semana_elegido).first()

        if not horario_dia:
            messages.error(request, f"Lo sentimos, no abrimos los días {dia_semana_elegido}. Por favor elige otro día.")
            return redirect('agendar_cita')

        # 4. Verificar si la hora está dentro del rango de apertura y cierre
        if not (horario_dia.horario_apertura <= hora_obj <= horario_dia.horario_cierre):
            messages.error(
                request, 
                f"El horario de atención para el {dia_semana_elegido} es de {horario_dia.horario_apertura.strftime('%H:%M')} a {horario_dia.horario_cierre.strftime('%H:%M')}."
            )
            return redirect('agendar_cita')

        # 5. Si pasa todas las validaciones, ¡Guardamos la cita!
        from .models import Cita # Asegúrate de importar el modelo
        Cita.objects.create(
            nombre_cliente=nombre,
            telefono=telefono,
            fecha=fecha_obj,
            hora=hora_obj,
            motivo=motivo
        )
        
        messages.success(request, "¡Tu cita ha sido agendada con éxito!")
        return redirect('inicio')

    return render(request, 'optica/agendar_cita.html', {
        'horarios': horarios_disponibles
    })