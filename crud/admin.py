from django.contrib import admin
from .models import *
# Register your models here.
class ProveedorAdmin(admin.ModelAdmin):
    readonly_fields = ('id','created_at','updated_at')
    list_display = ('id','proveedor')
    ordering = ['proveedor']
  
class ProductoAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at','updated_at')
    list_display = ('idProducto','name','proveedor','tipo','value','stock')
    ordering = ['name','proveedor']

class TipoProductoAdmin(admin.ModelAdmin):
    readonly_fields = ('id','created_at','updated_at')
    list_display = ('id','tipo')
    ordering = ['tipo']

 

admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(TipoProducto, TipoProductoAdmin)

