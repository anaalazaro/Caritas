from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction

@login_required
def delete_account(request):
    if request.method == 'POST':
        with transaction.atomic():
            user = request.user
            user.delete()
            messages.success(request,'La cuenta ha sido eliminada exitosamente.')
            return redirect('Inicio')#pagina de inicio


    
# Create your views here.
