from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from app.models import CustomUser
from .utils import send_otp
from datetime import datetime
import pyotp

# Create your views here.
def login_otp(request):
    error_message=None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            send_otp(request)
            request.session['username'] = username
            return redirect('otp')
        else:
            error_message = 'Usuario o contraseña inválidos'
    return render(request, 'login_otp.html', {'error_message': error_message})

def otp(request):
    error_message=None
    if request.method == 'POST':
        otp = request.POST['otp']
        username = request.session['username']

        otp_secret_key = request.session['otp_secret_key']
        otp_valid_until = request.session['otp_valid_date']

        if otp_secret_key and otp_valid_until is not None:
            valid_until = datetime.fromisoformat(otp_valid_until)
            if valid_until > datetime.now():
                totp = pyotp.TOTP(otp_secret_key, interval=120)
                if totp.verify(otp):
                    user = get_object_or_404(CustomUser, username=username)
                    login(request, user)

                    del request.session['otp_secret_key']
                    del request.session['otp_valid_date']

                    return redirect('main') #VA AL MAIN INVENTADO COMO PLACEHOLDER - UNA VEZ QUE ESTÉ TODO, DEBERÍA IR A LA PÁGINA QUE CORRESPONDA
                else:
                    error_message = 'OTP inválido'
            else:
                error_message = 'El OTP ha expirado'
        else:
            error_message = 'Ups... algo ha salido mal'
    return render(request, 'otp.html', {'error_message': error_message})

@login_required
def main_view(request):
    return render(request, 'main.html', {})
