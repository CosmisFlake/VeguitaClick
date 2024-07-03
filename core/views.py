from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Customer, Product, Order, OrderItem, TipoEnvio, ShippingAdress
from crud.models import Producto, Proveedor
from .utils import cookieCart, cartData, guestOrder
from django.http import JsonResponse
import json
import datetime

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def products(request):
    data = cartData(request)
    cartItems = data['cartItems']
            
    products = Product.objects.all()    
    context = {'products':products, 'cartItems':cartItems}
    return render(request, 'core/products.html', context)

def carrito(request):
    
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
        
        
    context = {'items':items, 'order':order, 'cartItems':cartItems}
    return render(request,'core/carrito.html', context)

def envios(request):
    
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items':items, 'order':order, 'cartItems':cartItems, 'shipping':False, 'tipo_envio':TipoEnvio.objects.all()}
    return render(request,'core/envios.html', context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Accion:', action)
    print('Product:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    
    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('El producto fue añadido', safe=False)

def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
         customer = request.user.customer
         order, created = Order.objects.get_or_create(customer=customer, complete=False)
        

    else:
        customer, order = guestOrder(request, data)

    total = int(data['form']['total'])
    order.transaction_id = transaction_id

    if total == int(order.get_cart_total):
        order.complete = True
    order.save() 
     
    if order.shipping == True:
        ShippingAdress.objects.create(
            customer=customer,
            order=order,
            address=data['shipping']['address'],
            city=data['shipping']['city'],
            rut=data['shipping']['rut'],
        )
             
     
    return JsonResponse('Pago satisfactorio!', safe=False)

def login (request):
    login(request)
    return redirect('core/inicioSesion.html')

def exit (request):
    logout(request)
    return redirect('home')  


