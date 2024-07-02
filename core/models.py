from django.db import models
from django.contrib.auth.models import User


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    # amount = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - ${self.amount}'

class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    adress = models.CharField(max_length=100)

    def __str__(self):
        return self.name
<<<<<<< HEAD

class Carrier(models.Model):
    name = models.CharField(max_length=100)
    adress = models.CharField(max_length=100)
    rut = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class ProductType(models.Model):
    tipo = models.CharField(verbose_name='Tipo de Producto', max_length=50)
    created_at = models.DateTimeField(verbose_name='Fecha creación', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Fecha actualización', auto_now=True)

    def __str__(self) -> str:
        return self.tipo    
class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nombre')
    price = models.IntegerField(verbose_name='Precio')
    tipo = models.ForeignKey(ProductType,verbose_name='Tipo de Producto',on_delete=models.CASCADE, null=True)
    digital = models.BooleanField(default=False, null=True, blank=False)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
    
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)
    
    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping = True
        return shipping        
    
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total
    
    
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)


    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

class TipoEnvio(models.Model):
    tipo = models.CharField(verbose_name='Tipo de Envio', max_length=50)
    created_at = models.DateTimeField(verbose_name='Fecha creación', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Fecha actualización', auto_now=True)

    def __str__(self) -> str:
        return self.tipo
    
class ShippingAdress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False, verbose_name='Direccion')
    city = models.CharField(max_length=200, null=False, verbose_name='Comuna')
    tipo_envio = models.ForeignKey(TipoEnvio, on_delete=models.SET_NULL, null=True)
    rut = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address



=======
>>>>>>> master
