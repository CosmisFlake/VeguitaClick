from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('products/', products, name='products'),
    path('carrito/', carrito, name='carrito'),
    path('envios/', envios, name='envios'),
    path('update_item/', updateItem, name='update_item'),
    path('process_order/', processOrder, name='process_order'),
    path('logout/', exit, name='exit'),
    path('inicioSesion/', login, name='login'),
]