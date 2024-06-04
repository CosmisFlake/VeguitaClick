from django.db import models

# Create your models here.
class Proveedor(models.Model):
    proveedor = models.CharField(verbose_name='Proveedor', max_length=50)
    created_at = models.DateTimeField(verbose_name='Fecha creación', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Fecha actualización', auto_now=True)

    class Meta:
        verbose_name = 'proveedor'
        verbose_name_plural = 'proveedores'


    def __str__(self) -> str:
        return self.proveedor


class Producto(models.Model):
    idProducto = models.CharField(primary_key=True,verbose_name='ID',max_length=20)
    name = models.CharField(verbose_name='Nombre',max_length=250)
    tipo = models.CharField(verbose_name='Tipo de Producto',max_length=100)
    proveedor = models.ForeignKey(Proveedor,verbose_name='Proveedor',on_delete=models.CASCADE)
    value = models.IntegerField(verbose_name='Valor')
    stock = models.IntegerField(verbose_name='Stock')
    image = models.ImageField(verbose_name='Imagen',upload_to='producto',null=True,blank=True)    
    created_at = models.DateTimeField(verbose_name='Fecha creación', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Fecha actualización', auto_now=True)

    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'
    

    def __str__(self) -> str:
        return self.name
