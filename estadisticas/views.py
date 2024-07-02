from django.shortcuts import render
from .forms import DateRangeForm,FilialForm
from solicitarIntercambio.models import Intercambio
from crearFilial.models import Filial
from django.db import models
from django.db.models import F, Count, Func
from django.utils import timezone 
import plotly.express as px
import pandas as pd
from datetime import datetime,timedelta
from django.utils import timezone


class TruncDate(Func):
    function = 'DATE'
    template = '%(function)s(%(expressions)s)'

def get_exchange_data(start_date, end_date, filial):
    start_date = datetime.combine(start_date, datetime.min.time())
    end_date = datetime.combine(end_date, datetime.min.time())
    """Obtiene la cantidad de intercambios entre dos fechas."""
    # Asegurarse de que las fechas son conscientes de la zona horaria
    start_date = timezone.make_aware(start_date, timezone.get_current_timezone())
    end_date = timezone.make_aware(end_date, timezone.get_current_timezone())
    
    # Anotar y usar F expresiones para extraer la parte de la fecha
    intercambios = Intercambio.objects.filter(fecha_solicitud__range=[start_date - timedelta(days=1), end_date + timedelta(days=1)], filial=filial, estado = 'Efectuado') \
                                      .values('fecha_solicitud__date') \
                                      .annotate(cantidad=Count('id'))
   
    df = pd.DataFrame(intercambios)
    if not intercambios:
        return df
    # Convertir  a tipo datetime
    df['Fecha'] = pd.to_datetime(df['fecha_solicitud__date'])
    
    # Crear un índice de fechas con todas las fechas entre fecha_desde y fecha_hasta
    date_range = pd.date_range(start=start_date.date(), end=end_date.date())
    all_dates_df = pd.DataFrame({'Fecha': date_range})
    
    # Fusionar los DataFrames usando set_index y reindex para asegurar todas las fechas están representadas
    df.set_index('Fecha', inplace=True)
    all_dates_df.set_index('Fecha', inplace=True)
    df = all_dates_df.join(df, how='left')
    
    # Llenar NaNs con 0 para las fechas sin intercambios
    df['cantidad'].fillna(0, inplace=True)
    
    # Resetear el índice
    df.reset_index(inplace=True)
    
    # Ordenar por fecha para garantizar el orden correcto en el gráfico
    df.sort_values(by='Fecha', inplace=True)
    
    return df

def estadisticas_periodo_tiempo(request):
    form = DateRangeForm()
    chart_div = None
    error_message = None
    if request.method == 'POST':
        form = DateRangeForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['fecha_desde']
            end_date = form.cleaned_data['fecha_hasta']
            filial = form.cleaned_data['filial']
            print(filial)
            df = get_exchange_data(start_date, end_date,filial)
            print(df,'hola')
            
            if not df.empty:
                df['Fecha'] = pd.to_datetime(df['Fecha'])  # Convertir a tipo datetime si es necesario
                df['Fecha'] = df['Fecha'].dt.strftime('%Y-%m-%d')  # Formatear fecha como string '%Y-%m-%d'
                fig = px.line(df, x='Fecha', y= 'cantidad', title=f'Cantidad de Intercambios entre las fechas {start_date.strftime("%d/%m/%Y")} y {end_date.strftime("%d/%m/%Y")}')
                chart_div = fig.to_html(full_html=False)
            else:
                error_message = "No hay intercambios solicitados para la filial seleccionada."

    return render(request, 'estadisticasDinamicas.html', {
        'form': form,
        'chart_div': chart_div,
        'error_message': error_message,
    })

def estadisticas_por_filial(request):
    chart_div = None
    error_message = None
    filiales = Filial.objects.filter(ayudante__isnull=False)
    print(filiales)
    if filiales:         
        intercambios = Intercambio.objects.filter(filial__in=filiales, estado = 'Efectuado') \
                                .values('filial__nombre') \
                                .annotate(cantidad=Count('id'))

        df = pd.DataFrame(intercambios)

        if not df.empty:
            df.rename(columns={'filial__nombre': 'filial'}, inplace=True)
            fig = px.bar(df, x='filial', y= 'cantidad', title=f'Cantidad de Intercambios por filial')
            chart_div = fig.to_html(full_html=False)
        else:
            error_message = "No hay intercambios solicitados para la filial seleccionada."

    return render(request, 'estadisticasPorFilial.html', {
        'chart_div': chart_div,
        'error_message': error_message,
    })