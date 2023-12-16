from tienda.models import Producto

CART_SESSION_ID = 'carro'


class Carro:
    def __init__(self, request):
        self.session = request.session
        self.carro = self.add_cart_session()

    def __iter__(self):
        producto_ids = self.carro.keys()
        productos = Producto.objects.filter(id__in=producto_ids)
        carro = self.carro.copy()
        for producto in productos:
            carro[str(producto.id)]['producto'] = producto
        for item in carro.values():
            item['valor_total'] = int(item['precio']) * int(item['quantity'])
            yield item

    def add_cart_session(self):
        carro = self.session.get(CART_SESSION_ID)
        if not carro:
            carro = self.session[CART_SESSION_ID] = {}
        return carro

    def añadir(self, producto, quantity):
        producto_id = str(producto.id)

        if producto_id not in self.carro:
            self.carro[producto_id] = {'quantity': 0, 'precio': str(producto.precio)}

        self.carro.get(producto_id)['quantity'] += quantity
        self.save()

    def borrar(self, producto):
        producto_id = str(producto.id)
        if producto_id in self.carro:
            del self.carro[producto_id]
            self.save()

    def guardar(self):
        self.session.modified = True

    def get_precio_total(self):
        return sum(int(item['precio']) * item['quantity'] for item in self.carro.values())

    def clear(self):
        del self.session[CART_SESSION_ID]
        self.save()