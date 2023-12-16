from django.urls import path
from tienda import views

app_name = 'tienda'

urlpatterns = [
    path('', views.pagina_inicio, name='pagina_inicio'),
    path('<slug:slug>', views.detalle_producto, name='detalle_producto'),
    path('agregar/favoritos/<int:producto_id>', views.añadir_favoritos, name='añadir_favoritos'),
    path('eliminar/favoritos/<int:producto_id>/', views.eliminar_favoritos, name='eliminar_favoritos'),
	path('favoritos/', views.favoritos, name='favoritos'),
	path('buscar/', views.buscar, name='buscar'),
	path('filtro/<slug:slug>/', views.filtro_por_categoria, name='filtro_por_categoria'),
]