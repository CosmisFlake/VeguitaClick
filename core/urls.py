from django.urls import path, include
from .views import *


app_name = 'rest_framework_api'

urlpatterns = [
    path('', home, name='home'),
    path('api/', include('rest_framework.urls')),
    path('inventario/', inventario, name='inventario'),
    path('logout/', exit, name='exit'),
    path('inicioSesion/', login, name='login'),
    path('api/payments/', PaymentListCreateAPIView.as_view(), name='payment-list'),
    path('api/payments/<int:pk>/', PaymentRetrieveUpdateDestroyAPIView.as_view(), name='payment-detail'),
]