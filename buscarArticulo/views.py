from django.shortcuts import render
from cargarArticulo.models import Articulo
# Create your views here.


def buscar_articulos(request):
    query = request.GET.get('q')
    resultados = None
    if query:
        resultados = Articulo.objects.filter(Titulo__icontains=query,aprobado=True, borrado=False)
    else:
        resultados = Articulo.objects.all()
    return render(request, 'buscarArticulo.html', {'resultados': resultados})

