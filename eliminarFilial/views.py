from django.shortcuts import render, redirect, get_object_or_404
from crearFilial.models import Filial

def eliminar_filial(request, filial_id):
    filial = get_object_or_404(Filial, id=filial_id)
    if request.method == 'POST':
        filial.delete()
        return redirect('listarFiliales')
    return render(request, 'eliminar_filial.html', {'filial': filial})