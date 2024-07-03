from django.shortcuts import render
from crearFilial.models import Filial
import json

def listar_filiales(request):
    filiales = Filial.objects.filter(borrado=False)

    # Construir una lista de diccionarios con los datos necesarios
    filiales_coords = []
    for filial in filiales:
        filiales_coords.append({
            'nombre': filial.nombre,
            'latitud': filial.latitud,
            'longitud': filial.longitud,
        })

    # Generar el código JavaScript para el mapa
    map_script = """
    <script>
        document.addEventListener('DOMContentLoaded', function () {
            var map = L.map('map').setView([-34.9216, -57.9544], 12); // Coordenadas de Plaza Moreno
            L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
            }).addTo(map);
    """

    for filial in filiales_coords:
        map_script += f"""
            L.marker([{filial['latitud']}, {filial['longitud']}]).addTo(map)
                .bindPopup("{filial['nombre']}");
        """

    map_script += """
        });
    </script>
    """

    return render(request, 'listar_filiales.html', {'filiales': filiales, 'map_script': map_script})
