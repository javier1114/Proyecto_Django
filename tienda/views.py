from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from tienda.models import Producto, Categoria
from carro.forms import QuantityForm

# Create your views here.
def paginat(request, list_object):
    p = Paginator(list_object, 15)
    numero_pagina = request.GET.get('page')
    try:
        page_obj = p.get_page(numero_pagina)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    return page_obj

def pagina_inicio(request):
    productos = Producto.objects.all()
    context = {'productos': paginat(request, productos)}
    return render(request, 'pagina_inicio.html', context)

@login_required
def detalle_producto(request, slug):
    form = QuantityForm()
    producto = get_object_or_404(Producto, slug=slug)
    related_products = Producto.objects.filter(categoria=producto.categoria).all()[:5]
    context = {
        'titulo':producto.titulo,
		'producto':producto,
		'form':form,
		'favoritos':'favoritos',
		'related_products':related_products
    }
    if request.user.likes.filter(id=producto.id).first():
        context['favoritos'] = 'borrar'
    return render(request,'detalle_producto.html', context)

@login_required
def añadir_favoritos(request, producto_id):
	producto = get_object_or_404(Producto, id=producto_id)
	request.User.likes.add(producto)
	return redirect('tienda:detalle_producto', slug=producto.slug)

@login_required
def eliminar_favoritos(request, producto_id):
	producto = get_object_or_404(Producto, id=producto_id)
	request.user.likes.remove(producto)
	return redirect('tienda:favoritos')

@login_required
def favoritos(request):
	productos = request.user.likes.all()
	context = {'title':'Favoritos', 'productos':productos}
	return render(request, 'favoritos.html', context)

def buscar(request):
	query = request.GET.get('q')
	productos = Producto.objects.filter(titulo__icontains=query).all()
	context = {'productos': paginat(request ,productos)}
	return render(request, 'pagina_inicio.html', context)


def filtro_por_categoria(request, slug):
	#El usuario da clic en las categorias y se desplegan las categorias con subcategorias
	result = []
	categoria = Categoria.objects.filter(slug=slug).first()
	[result.append(producto) \
		for producto in Producto.objects.filter(categoria=categoria.id).all()]
	# se comprueba si la categoria es padre de las subcategorias
	if not categoria.is_sub:
		sub_categorias = categoria.sub_categorias.all()
		# se obtienen las subcategorias de todas las categorias
		for categoria in sub_categorias:
			[result.append(producto) \
				for producto in Producto.objects.filter(categoria=categoria).all()]
	context = {'productos': paginat(request ,result)}
	return render(request, 'pagina_inicio.html', context)