from django.urls import path
from orden import views

app_name = 'orders'

urlpatterns = [
    path('crear', views.crear_orden, name='crear_orden'),
    path('lista', views.orden_usuario, name='orden_usuario'),
    path('checkout/<int:order_id>', views.checkout, name='checkout'),
    path('fake-payment/<int:order_id>', views.fake_payment, name='pay_order')
]