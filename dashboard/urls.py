from django.urls import path

from dashboard import views

app_name = 'dashboard'

urlpatterns = [
    path('productos', views.productos, name='productos'),
    path('productos/borrar/<int:id>', views.borrar_producto, name='borrar_producto'),
    path('productos/editar/<int:id>', views.editar_producto, name='editar_producto'),
    path('orden', views.orden, name='orden'),
    path('orden/detalle/<int:id>', views.orden_detalle, name='orden_detalle'),
    path('agregar_producto/', views.agregar_producto, name='agregar_producto'),
    path('agregar_categoria/', views.agregar_categoria, name='agregar_categoria'),
]