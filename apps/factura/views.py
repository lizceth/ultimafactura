from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.utils import timezone
from django.views.generic import TemplateView
from django.core import serializers
from django.db import connection
from .forms import ProductoForm, ClienteForm, CategoriaForm
from .models import Producto, Cliente, CategoriaProducto
import json
# Create your views here.


@login_required
def facturaCrear(request):
    message = None
    mess_tipo = 0
    sqfactura = 1
    form = None
    return render_to_response('facturacion/crear_factura.html', {'message': message, 'form': form, 'mess_tipo': mess_tipo, 'sqfactura': sqfactura}, context_instance=RequestContext(request))


def clientes(request):
    cliente=Cliente.objects.all()
    return render(request, 'facturacion/clientes.html',{'cliente':cliente})

def clienteAdd(request):
    if request.method=='POST':
        formulario=ClienteForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/clientes')
    else:
        formulario=ClienteForm()
    return render_to_response('facturacion/clienteAdd.html',
                              {'formulario':formulario},
                              context_instance=RequestContext(request))
def clienteEdit (request, id):
        cliente_edit= Cliente.objects.get(pk=id)
        if request.method == 'POST':
            formulario = ClienteForm(request.POST, instance = cliente_edit)
            if formulario.is_valid():
                formulario.save()
                return HttpResponseRedirect("/clientes")
        else:
            formulario = ClienteForm(instance= cliente_edit)
        return render_to_response('facturacion/clienteEdit.html',
                    {'formulario': formulario},
                    context_instance = RequestContext(request))
def clienteDelete (request, id):
    cliente_delete = get_object_or_404(Cliente, pk=id)
    cliente_delete.delete()
    return HttpResponseRedirect("/clientes")

def productos(request):
    productos=Producto.objects.all()
    return render(request, 'facturacion/productos.html',
                      {'productos':productos})


def productoAdd(request):
    if request.method=='POST':
        formulario=ProductoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/productos')
    else:
        formulario=ProductoForm()
        return render_to_response('facturacion/productoAdd.html',
                                  {'formulario':formulario},
                                  context_instance=RequestContext(request))

def productoEdit (request, id):
        producto_edit= Producto.objects.get(pk=id)
        if request.method == 'POST':
            formulario = ProductoForm(request.POST, instance = producto_edit)
            if formulario.is_valid():
                formulario.save()
                return HttpResponseRedirect("/productos")
        else:
            formulario = ProductoForm(instance= producto_edit)
        return render_to_response('facturacion/productoEdit.html',
                    {'formulario': formulario},
                    context_instance = RequestContext(request))

def productoDelete (request, id):
    producto_delete = get_object_or_404(Producto, pk=id)
    producto_delete.delete()
    return HttpResponseRedirect("/productos")

def categoria(request):
    productos=CategoriaProducto.objects.all()
    return render(request, 'facturacion/categoria.html',
                      {'categoria':categoria})


def categoriaAdd(request):
    if request.method=='POST':
        formulario=CategoriaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/categorias')
    else:
        formulario=CategoriaForm()
        return render_to_response('facturacion/categoriaAdd.html',
                                  {'formulario':formulario},
                                  context_instance=RequestContext(request))

def categoriaEdit (request, id):
        categoria_edit=CategoriaProducto.objects.get(pk=id)
        if request.method == 'POST':
            formulario =CategoriaForm(request.POST, instance = producto_edit)
            if formulario.is_valid():
                formulario.save()
                return HttpResponseRedirect("/categorias")
        else:
            formulario = CategoriaForm(instance= categoria_edit)
        return render_to_response('facturacion/categoriaEdit.html',
                    {'formulario': formulario},
                    context_instance = RequestContext(request))

def categoriaDelete (request, id):
    categoria_delete = get_object_or_404(CategoriaProducto, pk=id)
    categoria_delete.delete()
    return HttpResponseRedirect("/categorias")
