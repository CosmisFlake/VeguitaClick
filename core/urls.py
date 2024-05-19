from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('products/', products, name='products'),
    path('logout/', exit, name='exit'),
    path('inicioSesion/', login, name='login'),
    path('api/payments/', PaymentListCreateAPIView.as_view(), name='payment-list'),
    path('api/payments/<int:pk>/', PaymentRetrieveUpdateDestroyAPIView.as_view(), name='payment-detail'),
]