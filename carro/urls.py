from django.urls import path

from carro import views

app_name = 'carro'

urlpatterns = [
    path('añadir/<producto_id>/', views.añadir_al_carrito, name='añadir_al_carrito'),
    path('eliminar/<producto_id>/', views.eliminar_del_carro, name='eliminar_del_carro'),
    path('lista/', views.mostrar_carro, name='mostrar_carro'),
]