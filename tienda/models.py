from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify

# Create your models here.
class Categoria(models.Model):
    titulo = models.CharField(max_length = 200)
    sub_categoria = models.ForeignKey('self', 
                                      on_delete = models.CASCADE, related_name='sub_categorias', 
                                      null=True, blank=True)
    is_sub = models.BooleanField(default=False)
    slug = models.SlugField(max_length=200, unique = True, default=True)

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('tienda:detalle_producto', kwargs={'slug':self.slug})

    def save(self, *args, **kwargs): # new
        self.slug = slugify(self.titulo)
        return super().save(*args, **kwargs)
    
class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='categoria')
    imagen = models.ImageField(upload_to='productos')
    titulo = models.CharField(max_length=250)
    descripcion = models.TextField()
    precio = models.IntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)
    
    class Meta:
        ordering = ('-fecha_creacion',)

    def __str__(self):
        return self.slug
    
    def get_absolute_url(self):
        return reverse('tienda:detalle_producto', kwargs={'slug':self.slug})
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.titulo)
        return super().save(*args, **kwargs)