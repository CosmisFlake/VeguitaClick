from django.urls import path
from .views import *

urlpatterns = [
    path('', homeCore, name='homeCore'),
    path('register/', registerPage, name='register'),
    path('accounts/login/', loginPage, name='login'),
    path('accounts/logout/', logoutUser, name='logout'),
    path('products/', products, name='products'),
    path('carrito/', carrito, name='carrito'),
    path('envios/', envios, name='envios'),
    path('update_item/', updateItem, name='update_item'),
    path('process_order/', processOrder, name='process_order'),
]