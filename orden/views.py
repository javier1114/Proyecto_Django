from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from django.views.decorators.http import require_POST
from django.utils import timezone

from .models import Orden, OrderItem
from carro.utils.carro import Carro


@login_required
def crear_orden(request):
    carro = Carro(request)
    orden = Orden.objects.create(user=request.user)
    for item in carro:
        OrderItem.objects.create(
            orden=orden, producto=item['producto'],
            precio=item['precio'], quantity=item['quantity']
    )
    return redirect('orders:pay_order', order_id=orden.id)


@login_required
def checkout(request, orden_id):
    orden = get_object_or_404(Orden, id=orden_id)
    context = {'titulo':'Checkout' ,'orden':orden}
    return render(request, 'checkout.html', context)


@login_required
def fake_payment(request, orden_id):
    carro = Carro(request)
    carro.clear()
    orden = get_object_or_404(Orden, id=orden_id)
    orden.status = True
    orden.save()
    return redirect('orders:orden_usuario')


@login_required
def orden_usuario(request):
    orders = request.user.orders.all()
    context = {'titulo':'Orders', 'orders': orders}
    return render(request, 'orden_usuario.html', context)