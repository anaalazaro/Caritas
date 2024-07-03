from django.shortcuts import render, redirect, get_object_or_404
from crearFilial.models import Filial
from solicitarIntercambio.models import Intercambio
from django.contrib import messages
def eliminar_filial(request, filial_id):
    filial = get_object_or_404(Filial, id=filial_id)
    if request.method == 'POST':
        intercambios_filial= Intercambio.objects.filter(filial=filial_id, estado='Aceptado')
        if not intercambios_filial.exists():
            if filial.ayudante is not None:
                filial.ayudante.borrado=True
                filial.ayudante.save()
            filial.borrado=True
            filial.save()
            messages.success(request, "Se eliminó la filial exitosamente")
        else:
            messages.success(request, "No puedes eliminar la filial ya que posee intercambios pendientes a efectuar")
        return redirect('listarFiliales')
    return render(request, 'eliminar_filial.html', {'filial': filial})