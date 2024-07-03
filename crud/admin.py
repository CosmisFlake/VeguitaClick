from django.contrib import admin
from .models import *
# Register your models here.
class ProveedorAdmin(admin.ModelAdmin):
    readonly_fields = ('id','created_at','updated_at')
    list_display = ('id','proveedor','direccion','rut',)
    ordering = ['proveedor']
  
class ProductoAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at','updated_at')
    list_display = ('idProducto','name','proveedor','tipo','value','stock')
    ordering = ['name','proveedor']

class TipoProductoAdmin(admin.ModelAdmin):
    readonly_fields = ('id','created_at','updated_at')
    list_display = ('id','tipo')
    ordering = ['tipo']
    
class TipoPesoAdmin(admin.ModelAdmin):
    readonly_fields = ('id','created_at','updated_at')
    list_display = ('id','tipo_peso')
    ordering = ['tipo_peso']

class TipoVehiculoAdmin(admin.ModelAdmin):
    readonly_fields = ('id','created_at','updated_at')
    list_display = ('id','tipo')
    ordering = ['id']

class EstadoVehiculoAdmin(admin.ModelAdmin):
    readonly_fields = ('id','created_at','updated_at')
    list_display = ('id','estado')
    ordering = ['id']

class VehiculoAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at','updated_at')
    list_display = ('idVehiculo','nombre','tipo','color','estado')
    ordering = ['idVehiculo']

class TransportistaAdmin(admin.ModelAdmin):
    readonly_fields = ('id','created_at','updated_at')
    list_display = ('nombre','direccion','rut')
    ordering = ['nombre']

class ClienteAdmin(admin.ModelAdmin):
    readonly_fields = ('id','created_at','updated_at')
    list_display = ('nombre','direccion','rut','email')
    ordering = ['nombre']
 

admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(TipoProducto, TipoProductoAdmin)
admin.site.register(TipoPeso, TipoPesoAdmin)
admin.site.register(TipoVehiculo, TipoVehiculoAdmin)
admin.site.register(EstadoVehiculo, EstadoVehiculoAdmin)
admin.site.register(Vehiculo, VehiculoAdmin)
admin.site.register(Transportista, TransportistaAdmin)
admin.site.register(Cliente, ClienteAdmin)