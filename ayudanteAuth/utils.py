import pyotp
from django.core.mail import send_mail
from datetime import datetime, timedelta

def send_otp(request, custom_user):
    totp = pyotp.TOTP(pyotp.random_base32(), interval=120)
    otp = totp.now()
    request.session['otp_secret_key'] = totp.secret
    valid_date = datetime.now() + timedelta(minutes=2)
    request.session['otp_valid_date'] = str(valid_date)
    print(f"Su clave de uso único es {otp}")
    send_mail(
        'Tu OTP',
        f'Tu contraseña de uso único es: {otp}',
        'ingecaritas@gmail.com',
        [custom_user.email],
        fail_silently=False,
    )