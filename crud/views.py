from django.shortcuts import render, HttpResponse, redirect, reverse

from .models import *
from .forms import *

# Create your views here.
def root(request):
    return redirect('producto/')

def producto_lista(request):
    context = {'producto': Producto.objects.all()}
    return render(request,'crud/producto.html',context)

def producto_new(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            idProducto = form.cleaned_data.get('idProducto')
            name = form.cleaned_data.get('name')
            tipo = form.cleaned_data.get('tipo')
            proveedor = form.cleaned_data.get('proveedor')
            value = form.cleaned_data.get('value')
            stock = form.cleaned_data.get('stock')
            image = form.cleaned_data.get('image')
            obj = Producto.objects.create(
                idProducto = idProducto,
                name = name,
                tipo = tipo,
                proveedor = proveedor,
                value = value,
                stock = stock,
                image = image
            )
            obj.save()
            return redirect(reverse('producto')+ '?OK')
        else:
            return redirect(reverse('producto')+ '?FAIL')
    else:
        form = ProductoForm
    return render(request,'crud/producto-new.html',{'form':form})

def producto_update(request,producto_id):
    try:
        producto = Producto.objects.get(idProducto = producto_id)
        form = ProductoForm(instance=producto)

        if request.method == 'POST':
            form = ProductoForm(request.POST, request.FILES, instance=producto)
            if form.is_valid():
                form.save()
                return redirect(reverse('producto') + '?UPDATED')
            else:
                return redirect(reverse('producto-edit') + producto_id) 

        context = {'form':form}
        return render(request,'crud/producto-edit.html',context)
    except:
        return redirect(reverse('producto') + '?NO_EXISTS')


def producto_detail(request, producto_id):
    try:
        producto = Producto.objects.get(idProducto = producto_id )
        if producto:
            context = {'producto':producto}
            return render(request,'crud/producto-detail.html',context)
        else:
            return redirect(reverse('producto') + '?lala')
    except:
        return redirect(reverse('producto') + '?FAIL')
    

def producto_by_proveedor(request, proveedor):
    try:
        productos = Producto.objects.filter(proveedor=proveedor)
        if productos:
            context = {'productos':productos}
            return render(request,'crud/producto.html',context)
        else:
            return redirect(reverse('producto') + '?FAIL')
    except:
        return redirect(reverse('producto') + '?FAIL')
    

def producto_by_tipo(request, tipo):
    try:
        productos = Producto.objects.filter(tipo=tipo)
        if productos:
            context = {'productos':productos}
            return render(request,'crud/producto.html',context)
        else:
            return redirect(reverse('producto') + '?FAIL')
    except:
        return redirect(reverse('producto') + '?FAIL')
    
def producto_delete(request, producto_id):
    try:
        producto = Producto.objects.get(idProducto=producto_id)
        producto.delete()
        return redirect(reverse('producto') + '?DELETED')
    except:
        return redirect(reverse('producto') + '?FAIL')


