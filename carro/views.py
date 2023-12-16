from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from carro.utils.carro import Carro
from .forms import QuantityForm
from tienda.models import Producto

# Create your views here.
@login_required
def añadir_al_carrito(request, producto_id):
    carro = Carro(request)
    producto = get_object_or_404(Producto, id=producto_id)
    form = QuantityForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        carro.add(product=producto, quantity=data['quantity'])
        messages.success(request, 'Agregado al carrito!', 'info')
    return redirect('tienda:detalle_producto', slug=producto.slug)

@login_required
def mostrar_carro(request):
    carro = Carro(request)
    context = {'titulo': 'Carro', 'carro': carro}
    return render(request, 'carro.html', context)

@login_required
def eliminar_del_carro(request, producto_id):
    carro = Carro(request)
    producto = get_object_or_404(Producto, id=producto_id)
    carro.remove(producto)
    return redirect('carro:mostrar_carro')