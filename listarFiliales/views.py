from django.shortcuts import render
from django.shortcuts import render
from crearFilial.models import Filial

def listar_filiales(request):
    filiales = Filial.objects.all()
    return render(request, 'listar_filiales.html', {'filiales': filiales})
