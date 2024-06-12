from django.shortcuts import render, redirect
from .forms import FilialForm

def agregar_filial(request):
    if request.method == 'POST':
        form = FilialForm(request.POST)
        if form.is_valid():
            form.save()
            print(form)
            return redirect('listarFiliales')
    else:
        form = FilialForm()
    return render(request, 'agregar_filial.html', {'form': form})
