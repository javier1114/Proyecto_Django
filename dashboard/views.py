from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.http import Http404

from tienda.models import Producto
from cuentas.models import User
from orden.models import Orden, OrderItem
from .forms import AñadirProductoForm, AñadirCategoriaForm, EditarProductoForm


def is_manager(user):
    try:
        if not user.is_manager:
            raise Http404
        return True
    except:
        raise Http404


@user_passes_test(is_manager)
@login_required
def productos(request):
    productos = Producto.objects.all()
    context = {'titulo':'Productos' ,'productos':productos}
    return render(request, 'productos.html', context)


@user_passes_test(is_manager)
@login_required
def agregar_producto(request):
    if request.method == 'POST':
        form = AñadirProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto agregado con exito!')
            return redirect('dashboard:agregar_product')
    else:
        form = AñadirProductoForm()
    context = {'titulo':'Agregar producto', 'form':form}
    return render(request, 'agregar_producto.html', context)


@user_passes_test(is_manager)
@login_required
def borrar_producto(request, id):
    producto = Producto.objects.filter(id=id).delete()
    messages.success(request, 'El producto fue eliminado!', 'success')
    return redirect('dashboard:productos')


@user_passes_test(is_manager)
@login_required
def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        form = EditarProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Se han actualizado los detalles', 'success')
            return redirect('dashboard:productos')
    else:
        form = EditarProductoForm(instance=producto)
    context = {'titulo': 'Editar producto', 'form':form}
    return render(request, 'editar_producto.html', context)


@user_passes_test(is_manager)
@login_required
def agregar_categoria(request):
    if request.method == 'POST':
        form = AñadirCategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'La categoria ha sido añadida')
            return redirect('dashboard:agregar_categoria')
    else:
        form = AñadirCategoriaForm()
    context = {'titulo':'Agregar categoria', 'form':form}
    return render(request, 'agregar_categoria.html', context)


@user_passes_test(is_manager)
@login_required
def orden(request):
    orders = Orden.objects.all()
    context = {'titulo':'Pedidos procesados', 'orders':orders}
    return render(request, 'orden.html', context)


@user_passes_test(is_manager)
@login_required
def orden_detalle(request, id):
    orden = Orden.objects.filter(id=id).first()
    items = OrderItem.objects.filter(orden=orden).all()
    context = {'titulo':'Detalles del pedido', 'items':items, 'orden':orden}
    return render(request, 'orden_detalle.html', context)