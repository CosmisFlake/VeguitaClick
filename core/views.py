from django.shortcuts import render, redirect
from django.http import HttpResponseNotAllowed
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import CreateUserForm
from .utils import cookieCart, cartData, guestOrder
from django.http import JsonResponse
import json
import datetime

# Create your views here.
def homeCore(request):
    data = cartData(request)
    cartItems = data['cartItems']
            
    products = Product.objects.all()    
    context = {'products':products, 'cartItems':cartItems}
    return render(request, 'core/home.html', context)

def registerPage(request):
    form = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el usuario
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            
            user = authenticate(request, username=username, password=password)
            login(request, user)        
            messages.success(request, 'La cuenta fue creada para ' + username)
            return redirect('login')
        else:
            messages.error(request, 'Hubo un error al crear la cuenta')
            return redirect('register')
           
    else:      
        context = {'form':form}
        return render(request, 'accounts/register.html', context)

def loginPage(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homeCore')
        else:
            messages.info(request, 'Usuario o contraseña incorrectos')
    context = {}
    return render(request, 'accounts/login.html', context)

def logoutUser(request):
    if request.method == 'POST' or request.method == 'GET':
        logout(request)
        return redirect('login')
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])

@login_required(login_url='login')
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
         customer = request.username.customer
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
 


