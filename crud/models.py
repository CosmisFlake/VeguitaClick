from django.db import models

# Create your models here.
class Proveedor(models.Model):
    proveedor = models.CharField(verbose_name='Proveedor', max_length=50)
    direccion = models.CharField(verbose_name='Direccion',max_length=100)
    rut = models.CharField(verbose_name='Rut',max_length=12)
    created_at = models.DateTimeField(verbose_name='Fecha creación', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Fecha actualización', auto_now=True)

    class Meta:
        verbose_name = 'proveedor'
        verbose_name_plural = 'proveedores'
        ordering = ['proveedor']


    def __str__(self) -> str:
        return self.proveedor

class TipoProducto(models.Model):
    tipo = models.CharField(verbose_name='Tipo de Producto', max_length=50)
    created_at = models.DateTimeField(verbose_name='Fecha creación', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Fecha actualización', auto_now=True)

    class Meta:
        verbose_name = 'tipo de producto'
        verbose_name_plural = 'tipo de productos'
        ordering = ['id']


    def __str__(self) -> str:
        return self.tipo

class TipoPeso(models.Model):
    tipo_peso = models.CharField(verbose_name='Tipo de Peso', max_length=50)
    created_at = models.DateTimeField(verbose_name='Fecha creación', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Fecha actualización', auto_now=True)
    
    class Meta:
        verbose_name = 'tipo de peso'
        verbose_name_plural = 'tipo de pesos'
        ordering = ['id']


    def __str__(self) -> str:
        return self.tipo_peso  

class Producto(models.Model):
    idProducto = models.CharField(primary_key=True,verbose_name='ID',max_length=20)
    name = models.CharField(verbose_name='Nombre',max_length=250)
    tipo = models.ForeignKey(TipoProducto,verbose_name='Tipo de Producto',on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedor,verbose_name='Proveedor',on_delete=models.CASCADE)
    value = models.IntegerField(verbose_name='Valor')
    stock = models.IntegerField(verbose_name='Stock')
    peso = models.IntegerField(verbose_name='Peso', null=True, blank=True)
    tipo_peso = models.ForeignKey(TipoPeso,verbose_name='Tipo de Peso',on_delete=models.CASCADE, null=True)
    image = models.ImageField(verbose_name='Imagen',upload_to='producto',null=True,blank=True)    
    created_at = models.DateTimeField(verbose_name='Fecha creación', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Fecha actualización', auto_now=True)

    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'
    

    def __str__(self) -> str:
        return self.name


class TipoVehiculo(models.Model):
    tipo = models.CharField(verbose_name='Tipo de Vehiculo', max_length=50)
    created_at = models.DateTimeField(verbose_name='Fecha creación', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Fecha actualización', auto_now=True)

    class Meta:
        verbose_name = 'tipo de vehiculo'
        verbose_name_plural = 'tipo de vehiculos'
        ordering = ['id']


    def __str__(self) -> str:
        return self.tipo


class EstadoVehiculo(models.Model):
    estado = models.CharField(verbose_name='Estado de Vehiculo', max_length=50)
    created_at = models.DateTimeField(verbose_name='Fecha creación', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Fecha actualización', auto_now=True)

    class Meta:
        verbose_name = 'estado de vehiculo'
        verbose_name_plural = 'estado de vehiculos'
        ordering = ['id']


    def __str__(self) -> str:
        return self.estado


class Vehiculo(models.Model):
    idVehiculo = models.CharField(primary_key=True,verbose_name='ID',max_length=20)
    nombre = models.CharField(verbose_name='Nombre',max_length=250)
    tipo = models.ForeignKey(TipoVehiculo,verbose_name='Tipo de Vehiculo',on_delete=models.CASCADE)
    color = models.CharField(verbose_name='Color de Vehiculo',max_length=12)
    estado = models.ForeignKey(EstadoVehiculo,verbose_name='Estado de Vehiculo',on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='Imagen',upload_to='vehiculo',null=True,blank=True)  
    created_at = models.DateTimeField(verbose_name='Fecha creación', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Fecha actualización', auto_now=True)

    class Meta:
        verbose_name = 'vehiculo'
        verbose_name_plural = 'vehiculos'
        ordering = ['nombre']


    def __str__(self) -> str:
        return self.nombre


class Transportista(models.Model):
    nombre = models.CharField(verbose_name='Nombre',max_length=250)
    direccion = models.CharField(verbose_name='Direccion',max_length=100)
    rut = models.CharField(verbose_name='Rut',max_length=12)
    image = models.ImageField(verbose_name='Imagen',upload_to='transportista',null=True,blank=True)
    created_at = models.DateTimeField(verbose_name='Fecha creación', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Fecha actualización', auto_now=True)

    class Meta:
        verbose_name = 'transportista'
        verbose_name_plural = 'transportistas'
        ordering = ['nombre']


    def __str__(self) -> str:
        return self.nombre


class Cliente(models.Model):
    nombre = models.CharField(verbose_name='Nombre',max_length=250)
    direccion = models.CharField(verbose_name='Direccion',max_length=100)
    rut = models.CharField(verbose_name='Rut',max_length=12)
    email = models.EmailField(verbose_name='Email',max_length=200)
    created_at = models.DateTimeField(verbose_name='Fecha creación', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Fecha actualización', auto_now=True)

    class Meta:
        verbose_name = 'cliente'
        verbose_name_plural = 'clientes'
        ordering = ['nombre']


    def __str__(self) -> str:
        return self.nombre