from django.shortcuts import render, redirect
from django.urls import reverse
from needList.models import NeedList
from cargarArticulo.models import Articulo

def existeEnNeedList(articulo, usuario):
    return NeedList.objects.filter(articulo= articulo, usuario=usuario).exists()

# Create your views here.
from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages

def agregarArticuloANeedList(request, articulo_id):
    articulo = Articulo.objects.get(id=articulo_id)
    usuario = request.user

    if existeEnNeedList(articulo, usuario):
        messages.info(request, "Este artículo ya se encuentra registrado en su NeedList")
    else:
        needList = NeedList(articulo=articulo, usuario=usuario)
        needList.save()
        messages.success(request, "Artículo agregado a su NeedList")

    return redirect('menuPrincipal')

def verArticulosEnLaNeedList(request):
    needlists = NeedList.objects.filter(usuario=request.user)
    articulos = [needlist.articulo for needlist in needlists]
    return render(request, 'needList.html', {'articulos': articulos})

def borrarArticuloDeNeedList(request, articulo_id):
     articulo= Articulo.objects.get(pk= articulo_id)
     needlist_entry = NeedList.objects.get(articulo=articulo, usuario=request.user)
     needlist_entry.delete()
     messages.success(request, "Articulo borrado de NeedList")
     return redirect('menuPrincipal')

def confirmar_eliminar_articulo(request, articulo_id):
    return render(request, 'confirmacion.html', {'articulo': articulo_id})
