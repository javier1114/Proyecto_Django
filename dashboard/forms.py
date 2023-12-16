from django import forms
from django.forms import ModelForm

from tienda.models import Producto, Categoria


class AñadirProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ['categoria', 'imagen', 'titulo','descripcion', 'precio']
        labels = {
            'categoria': 'Elige una categoria o subcategoria:',
            'imagen': 'Imagen:',
            'titulo': 'Nombre producto:',
            'descripcion': 'Descripcion del producto:',
            'precio': 'Precio:'
        }

    def __init__(self, *args, **kwargs):
        super(AñadirProductoForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class AñadirCategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = ['titulo', 'sub_categoria', 'is_sub']
        labels = {
            'titulo': 'Nombre categoria',
            'sub_categoria': 'Subcategoría de...',
            'is_sub': '¿Es subcategoría?'
        }

    def __init__(self, *args, **kwargs):
        super(AñadirCategoriaForm, self).__init__(*args, **kwargs)
        self.fields['is_sub'].widget.attrs['class'] = 'form-check-input'
        self.fields['sub_categoria'].widget.attrs['class'] = 'form-control'
        self.fields['titulo'].widget.attrs['class'] = 'form-control'


class EditarProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ['categoria', 'imagen', 'titulo','descripcion', 'precio']
        labels = {
            'categoria': 'Elige una categoria o subcategoria:',
            'imagen': 'Imagen:',
            'titulo': 'Nombre producto:',
            'descripcion': 'Descripcion del producto:',
            'precio': 'Precio:'
        }

    def __init__(self, *args, **kwargs):
        super(EditarProductoForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'