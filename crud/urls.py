from django.urls import path
from .views import *

urlpatterns = [
    path('', root),
    path('producto/', producto_lista, name="producto"),    
    path('producto/<str:producto_id>/delete', producto_delete, name="producto-delete"),
    path('producto/detail/<str:producto_id>', producto_detail, name="producto-detail"),
    path('producto/edit/<str:producto_id>', producto_update, name="producto-edit"),
    path('producto/new/', producto_new, name="producto-new"),
    path('producto/proveedor/<proveedor>', producto_by_proveedor, name="producto-proveedor"),
    path('producto/tipo/<tipo>',producto_by_tipo, name="producto-tipo"),
]