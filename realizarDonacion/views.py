from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
import mercadopago

def donar(request):
    if request.method == 'POST':
        # Recuperar el monto desde el formulario
        monto = float(request.POST.get('monto', 0))  # Asegúrate de manejar adecuadamente la obtención del monto

        # Configurar credenciales de MercadoPago (Access Token del vendedor)
        mp = mercadopago.SDK("APP_USR-6328171704210541-063019-e668446d52b7057951f58da994c4e742-1881541468")

        try:
            # Crear preferencia de pago
            preference_data = {
                "items": [
                    {
                        "title": "Donación",
                        "quantity": 1,
                        "currency_id": "ARS",  # Cambiar según tu moneda
                        "unit_price": monto
                    }
                ],
                "back_urls": {
                    "success": "http://127.0.0.1:8000/",
                    "failure": "http://127.0.0.1:8000/",
                    "pending": "http://127.0.0.1:8000/"
                },
                "auto_return": "approved",
                "return_url": "http://127.0.0.1:8000/donar/"
            }
            preference = mp.preference().create(preference_data)

            # Verificar si 'init_point' está presente en la respuesta
            if 'init_point' in preference['response']:
                pago_url = preference['response']['init_point']
                return redirect(pago_url)
            else:
                # Manejar el caso donde 'init_point' no está presente en la respuesta
                error_message = "Error al obtener la URL de inicio del pago"
                # Puedes registrar este error o mostrar un mensaje genérico de error
                return render(request, 'error.html', {'error_message': error_message})

        except Exception as e:
            # Manejar cualquier excepción que pueda surgir durante la creación de la preferencia
            error_message = f"Error al crear la preferencia de pago: No se pudo establecer conexión con la API de MercadoPago"
            # Puedes registrar este error o mostrar un mensaje genérico de error
            return render(request, 'error.html', {'error_message': error_message})

    return render(request, 'donar.html')


"APP_USR-6328171704210541-063019-e668446d52b7057951f58da994c4e742-1881541468"
