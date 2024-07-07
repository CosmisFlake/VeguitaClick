from django.shortcuts import render, HttpResponse, redirect, reverse

from .models import *
from .forms import *
from core.models import *

# Create your views here.
def root(request):
    return redirect('producto/')

def home(request):
    return render(request, 'crud/home.html')

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


def tipoProducto_lista(request):
    context = {'tipoProducto': TipoProducto.objects.all()}
    return render(request,'crud/tipoProducto.html',context)


def tipoProducto_new(request):
    if request.method == 'POST':
        form = TipoProductoForm(request.POST, request.FILES)
        if form.is_valid():
            tipo = form.cleaned_data.get('tipo')
            obj = TipoProducto.objects.create(
                tipo = tipo
            )
            obj.save()
            return redirect(reverse('tipoProducto')+ '?OK')
        else:
            return redirect(reverse('tipoProducto')+ '?FAIL')
    else:
        form = TipoProductoForm
    return render(request,'crud/tipoProducto-new.html',{'form':form})


def tipoProducto_update(request,tipoProducto_id):
    try:
        tipoProducto = TipoProducto.objects.get(id = tipoProducto_id)
        form = TipoProductoForm(instance=tipoProducto)

        if request.method == 'POST':
            form = TipoProductoForm(request.POST, request.FILES, instance=tipoProducto)
            if form.is_valid():
                form.save()
                return redirect(reverse('tipoProducto') + '?UPDATED')
            else:
                return redirect(reverse('tipoProducto-edit') + tipoProductos_id) 

        context = {'form':form}
        return render(request,'crud/tipoProducto-edit.html',context)
    except:
        return redirect(reverse('tipoProducto') + '?NO_EXISTS')


def tipoProducto_detail(request, tipoProducto_id):
    try:
        tipoProducto = TipoProducto.objects.get(id = tipoProducto_id )
        if tipoProducto:
            context = {'tipoProducto':tipoProducto}
            return render(request,'crud/tipoProducto-detail.html',context)
        else:
            return redirect(reverse('tipoProducto') + '?lala')
    except:
        return redirect(reverse('tipoProducto') + '?FAIL')


def tipoProducto_delete(request, tipoProducto_id):
    try:
        tipoProducto = TipoProducto.objects.get(id=tipoProducto_id)
        tipoProducto.delete()
        return redirect(reverse('tipoProducto') + '?DELETED')
    except:
        return redirect(reverse('tipoProducto') + '?FAIL')


def tipoPeso_lista(request):
    context = {'tipoPeso': TipoPeso.objects.all()}
    return render(request,'crud/tipoPeso.html',context)


def tipoPeso_new(request):
    if request.method == 'POST':
        form = TipoPesoForm(request.POST, request.FILES)
        if form.is_valid():
            tipo_peso = form.cleaned_data.get('tipo_peso')
            obj = TipoPeso.objects.create(
                tipo_peso = tipo_peso
            )
            obj.save()
            return redirect(reverse('tipoPeso')+ '?OK')
        else:
            return redirect(reverse('tipoPeso')+ '?FAIL')
    else:
        form = TipoPesoForm
    return render(request,'crud/tipoPeso-new.html',{'form':form})


def tipoPeso_update(request,tipoPeso_id):
    try:
        tipoPeso = TipoPeso.objects.get(id = tipoPeso_id)
        form = TipoPesoForm(instance=tipoPeso)

        if request.method == 'POST':
            form = TipoPesoForm(request.POST, request.FILES, instance=tipoPeso)
            if form.is_valid():
                form.save()
                return redirect(reverse('tipoPeso') + '?UPDATED')
            else:
                return redirect(reverse('tipoPeso-edit') + tipoPeso_id) 

        context = {'form':form}
        return render(request,'crud/tipoPeso-edit.html',context)
    except:
        return redirect(reverse('tipoPeso') + '?NO_EXISTS')


def tipoPeso_detail(request, tipoPeso_id):
    try:
        tipoPeso = TipoPeso.objects.get(id = tipoPeso_id )
        if tipoPeso:
            context = {'tipoPeso':tipoPeso}
            return render(request,'crud/tipoPeso-detail.html',context)
        else:
            return redirect(reverse('tipoPeso') + '?lala')
    except:
        return redirect(reverse('tipoPeso') + '?FAIL')


def tipoPeso_delete(request, tipoPeso_id):
    try:
        tipoPeso = TipoPeso.objects.get(id=tipoPeso_id)
        tipoPeso.delete()
        return redirect(reverse('tipoPeso') + '?DELETED')
    except:
        return redirect(reverse('tipoPeso') + '?FAIL')


def proveedor_lista(request):
    context = {'proveedor': Proveedor.objects.all()}
    return render(request,'crud/proveedor.html',context)


def proveedor_new(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST, request.FILES)
        if form.is_valid():
            proveedor = form.cleaned_data.get('proveedor')
            direccion = form.cleaned_data.get('direccion')
            rut = form.cleaned_data.get('rut')
            obj = Proveedor.objects.create(
                proveedor = proveedor,
                direccion = direccion,
                rut = rut
            )
            obj.save()
            return redirect(reverse('proveedor')+ '?OK')
        else:
            return redirect(reverse('proveedor')+ '?FAIL')
    else:
        form = ProveedorForm
    return render(request,'crud/proveedor-new.html',{'form':form})


def proveedor_update(request, proveedor_id):
    try:
        proveedor = Proveedor.objects.get(id = proveedor_id)
        form = ProveedorForm(instance=proveedor)

        if request.method == 'POST':
            form = ProveedorForm(request.POST, request.FILES, instance=proveedor)
            if form.is_valid():
                form.save()
                return redirect(reverse('proveedor') + '?UPDATED')
            else:
                return redirect(reverse('proveedor-edit') + proveedor_id) 

        context = {'form':form}
        return render(request,'crud/proveedor-edit.html',context)
    except:
        return redirect(reverse('proveedor') + '?NO_EXISTS')


def proveedor_detail(request, proveedor_id):
    try:
        proveedor = Proveedor.objects.get(id = proveedor_id)
        if proveedor:
            context = {'proveedor':proveedor}
            return render(request,'crud/proveedor-detail.html',context)
        else:
            return redirect(reverse('proveedor') + '?lala')
    except:
        return redirect(reverse('proveedor') + '?FAIL')


def proveedor_delete(request, proveedor_id):
    try:
        proveedor = Proveedor.objects.get(id=proveedor_id)
        proveedor.delete()
        return redirect(reverse('proveedor') + '?DELETED')
    except:
        return redirect(reverse('proveedor') + '?FAIL')


def tipoVehiculo_lista(request):
    context = {'tipoVehiculo': TipoVehiculo.objects.all()}
    return render(request,'crud/tipoVehiculo.html',context)


def tipoVehiculo_new(request):
    if request.method == 'POST':
        form = TipoVehiculoForm(request.POST, request.FILES)
        if form.is_valid():
            tipo = form.cleaned_data.get('tipo')
            obj = TipoVehiculo.objects.create(
                tipo = tipo
            )
            obj.save()
            return redirect(reverse('tipoVehiculo')+ '?OK')
        else:
            return redirect(reverse('tipoVehiculo')+ '?FAIL')
    else:
        form = TipoVehiculoForm
    return render(request,'crud/tipoVehiculo-new.html',{'form':form})


def tipoVehiculo_update(request,tipoVehiculo_id):
    try:
        tipoVehiculo = TipoVehiculo.objects.get(id = tipoVehiculo_id)
        form = TipoVehiculoForm(instance=tipoVehiculo)

        if request.method == 'POST':
            form = TipoVehiculoForm(request.POST, request.FILES, instance=tipoVehiculo)
            if form.is_valid():
                form.save()
                return redirect(reverse('tipoVehiculo') + '?UPDATED')
            else:
                return redirect(reverse('tipoVehiculo-edit') + tipoVehiculo_id) 

        context = {'form':form}
        return render(request,'crud/tipoVehiculo-edit.html',context)
    except:
        return redirect(reverse('tipoVehiculo') + '?NO_EXISTS')


def tipoVehiculo_detail(request, tipoVehiculo_id):
    try:
        tipoVehiculo = TipoVehiculo.objects.get(id = tipoVehiculo_id )
        if tipoVehiculo:
            context = {'tipoVehiculo':tipoVehiculo}
            return render(request,'crud/tipoVehiculo-detail.html',context)
        else:
            return redirect(reverse('tipoVehiculo') + '?lala')
    except:
        return redirect(reverse('tipoVehiculo') + '?FAIL')


def tipoVehiculo_delete(request, tipoVehiculo_id):
    try:
        tipoVehiculo = TipoVehiculo.objects.get(id=tipoVehiculo_id)
        tipoVehiculo.delete()
        return redirect(reverse('tipoVehiculo') + '?DELETED')
    except:
        return redirect(reverse('tipoVehiculo') + '?FAIL')


def estadoVehiculo_lista(request):
    context = {'estadoVehiculo': EstadoVehiculo.objects.all()}
    return render(request,'crud/estadoVehiculo.html',context)


def estadoVehiculo_new(request):
    if request.method == 'POST':
        form = EstadoVehiculoForm(request.POST, request.FILES)
        if form.is_valid():
            estado = form.cleaned_data.get('estado')
            obj = EstadoVehiculo.objects.create(
                estado = estado
            )
            obj.save()
            return redirect(reverse('estadoVehiculo')+ '?OK')
        else:
            return redirect(reverse('estadoVehiculo')+ '?FAIL')
    else:
        form = EstadoVehiculoForm
    return render(request,'crud/estadoVehiculo-new.html',{'form':form})


def estadoVehiculo_update(request,estadoVehiculo_id):
    try:
        estadoVehiculo = EstadoVehiculo.objects.get(id = estadoVehiculo_id)
        form = EstadoVehiculoForm(instance=estadoVehiculo)

        if request.method == 'POST':
            form = EstadoVehiculoForm(request.POST, request.FILES, instance=estadoVehiculo)
            if form.is_valid():
                form.save()
                return redirect(reverse('estadoVehiculo') + '?UPDATED')
            else:
                return redirect(reverse('estadoVehiculo-edit') + estadoVehiculo_id) 

        context = {'form':form}
        return render(request,'crud/estadoVehiculo-edit.html',context)
    except:
        return redirect(reverse('estadoVehiculo') + '?NO_EXISTS')


def estadoVehiculo_detail(request, estadoVehiculo_id):
    try:
        estadoVehiculo = EstadoVehiculo.objects.get(id = estadoVehiculo_id )
        if estadoVehiculo:
            context = {'estadoVehiculo':estadoVehiculo}
            return render(request,'crud/estadoVehiculo-detail.html',context)
        else:
            return redirect(reverse('estadoVehiculo') + '?lala')
    except:
        return redirect(reverse('estadoVehiculo') + '?FAIL')


def estadoVehiculo_delete(request, estadoVehiculo_id):
    try:
        estadoVehiculo = EstadoVehiculo.objects.get(id=estadoVehiculo_id)
        estadoVehiculo.delete()
        return redirect(reverse('estadoVehiculo') + '?DELETED')
    except:
        return redirect(reverse('estadoVehiculo') + '?FAIL')


def vehiculo_lista(request):
    context = {'vehiculo': Vehiculo.objects.all()}
    return render(request,'crud/vehiculo.html',context)


def vehiculo_new(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST, request.FILES)
        if form.is_valid():
            idVehiculo = form.cleaned_data.get('idVehiculo')
            nombre = form.cleaned_data.get('nombre')
            tipo = form.cleaned_data.get('tipo')
            color = form.cleaned_data.get('color')
            estado = form.cleaned_data.get('estado')
            image = form.cleaned_data.get('image')
            obj = Vehiculo.objects.create(
                idVehiculo = idVehiculo,
                nombre = nombre,
                tipo = tipo,
                color = color,
                estado = estado,
                image = image
            )
            obj.save()
            return redirect(reverse('vehiculo')+ '?OK')
        else:
            return redirect(reverse('vehiculo')+ '?FAIL')
    else:
        form = VehiculoForm
    return render(request,'crud/vehiculo-new.html',{'form':form})


def vehiculo_update(request,vehiculo_id):
    try:
        vehiculo = Vehiculo.objects.get(idVehiculo = vehiculo_id)
        form = VehiculoForm(instance=vehiculo)

        if request.method == 'POST':
            form = VehiculoForm(request.POST, request.FILES, instance=vehiculo)
            if form.is_valid():
                form.save()
                return redirect(reverse('vehiculo') + '?UPDATED')
            else:
                return redirect(reverse('vehiculo-edit') + vehiculo_id) 

        context = {'form':form}
        return render(request,'crud/vehiculo-edit.html',context)
    except:
        return redirect(reverse('vehiculo') + '?NO_EXISTS')


def vehiculo_detail(request, vehiculo_id):
    try:
        vehiculo = Vehiculo.objects.get(idVehiculo = vehiculo_id )
        if vehiculo:
            context = {'vehiculo':vehiculo}
            return render(request,'crud/vehiculo-detail.html',context)
        else:
            return redirect(reverse('vehiculo') + '?lala')
    except:
        return redirect(reverse('vehiculo') + '?FAIL')


def vehiculo_delete(request, vehiculo_id):
    try:
        vehiculo = Vehiculo.objects.get(idVehiculo=vehiculo_id)
        vehiculo.delete()
        return redirect(reverse('vehiculo') + '?DELETED')
    except:
        return redirect(reverse('vehiculo') + '?FAIL')


def transportista_lista(request):
    context = {'transportista': Transportista.objects.all()}
    return render(request,'crud/transportista.html',context)


def transportista_new(request):
    if request.method == 'POST':
        form = TransportistaForm(request.POST, request.FILES)
        if form.is_valid():
            nombre = form.cleaned_data.get('nombre')
            direccion = form.cleaned_data.get('direccion')
            rut = form.cleaned_data.get('rut')
            image = form.cleaned_data.get('image')
            obj = Transportista.objects.create(
                nombre = nombre,
                direccion = direccion,
                rut = rut,
                image = image
            )
            obj.save()
            return redirect(reverse('transportista')+ '?OK')
        else:
            return redirect(reverse('transportista')+ '?FAIL')
    else:
        form = TransportistaForm
    return render(request,'crud/transportista-new.html',{'form':form})


def transportista_update(request,transportista_id):
    try:
        transportista = Transportista.objects.get(id = transportista_id)
        form = TransportistaForm(instance=transportista)

        if request.method == 'POST':
            form = TransportistaForm(request.POST, request.FILES, instance=transportista)
            if form.is_valid():
                form.save()
                return redirect(reverse('transportista') + '?UPDATED')
            else:
                return redirect(reverse('transportista-edit') + transportista_id) 

        context = {'form':form}
        return render(request,'crud/transportista-edit.html',context)
    except:
        return redirect(reverse('transportista') + '?NO_EXISTS')


def transportista_detail(request, transportista_id):
    try:
        transportista = Transportista.objects.get(id = transportista_id )
        if transportista:
            context = {'transportista':transportista}
            return render(request,'crud/transportista-detail.html',context)
        else:
            return redirect(reverse('transportista') + '?lala')
    except:
        return redirect(reverse('transportista') + '?FAIL')


def transportista_delete(request, transportista_id):
    try:
        transportista = Transportista.objects.get(id=transportista_id)
        transportista.delete()
        return redirect(reverse('transportista') + '?DELETED')
    except:
        return redirect(reverse('transportista') + '?FAIL')


def cliente_lista(request):
    context = {'cliente': Customer.objects.all()}
    return render(request,'crud/cliente.html',context)


def cliente_update(request,cliente_id):
    try:
        cliente = Customer.objects.get(id = cliente_id)
        form = CreateUserForm(instance=cliente)

        if request.method == 'POST':
            form = CreateUserForm(request.POST, request.FILES, instance=cliente)
            if form.is_valid():
                form.save()
                return redirect(reverse('cliente') + '?UPDATED')
            else:
                return redirect(reverse('cliente-edit') + cliente_id) 

        context = {'form':form}
        return render(request,'crud/cliente-edit.html',context)
    except:
        return redirect(reverse('cliente') + '?NO_EXISTS')


def cliente_detail(request, cliente_id):
    try:
        cliente = Customer.objects.get(id = cliente_id )
        if cliente:
            context = {'cliente':cliente}
            return render(request,'crud/cliente-detail.html',context)
        else:
            return redirect(reverse('cliente') + '?lala')
    except:
        return redirect(reverse('cliente') + '?FAIL')


def cliente_delete(request, cliente_id):
    try:
        cliente = Customer.objects.get(id=cliente_id)
        cliente.delete()
        return redirect(reverse('cliente') + '?DELETED')
    except:
        return redirect(reverse('cliente') + '?FAIL')