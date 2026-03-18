from datetime import datetime
from model import errores 

def validar_salario(salario):
    if not isinstance(salario, int):
        raise errores.ErrorSalarioNoEntero()
    if salario <= 0:
        raise errores.ErrorSalarioMenorDeCero()
    return True
    
formato_fecha = "%d/%m/%Y"

def convertir_fecha(fecha):
    if not fecha:
        raise errores.ErrorFechaFormatoIncorrecto()
    try:
        return datetime.strptime(fecha, formato_fecha)
    except ValueError:
        raise errores.ErrorFechaFormatoIncorrecto()
    
def validar_rango_fechas(inicio, fin):
    if fin < inicio: 
        raise errores.ErrorFechaIncorrecta()
    
def calcular_dias_360(fecha_inicio, fecha_fin):
    y1, m1, d1 = fecha_inicio.year, fecha_inicio.month, fecha_inicio.day
    y2, m2, d2 = fecha_fin.year, fecha_fin.month, fecha_fin.day

    return (y2 - y1) * 360 + (m2 - m1) * 30 + (d2 - d1)

def calcular_tiempo_trabajado_dias(inicio, fin):
    fecha_inicio = convertir_fecha(inicio)
    fecha_fin = convertir_fecha(fin)
    
    validar_rango_fechas(fecha_inicio, fecha_fin)
    
    return calcular_dias_360(fecha_inicio, fecha_fin)

def calcular_cesantias(salario, dias):
    return (salario*dias)/360
    
def calcular_interes_cesantias(cesantias, dias):
    return (cesantias*dias*0.12)/360

def calcular_vacaciones(salario,dias):
    return(salario*dias)/720

def calcular_prima_servicios(salario, dias):
    return(salario*dias)/360

def calcular_pago_neto(cesantias, interesCesantia, vacaciones, prima):
    return round(cesantias + interesCesantia + vacaciones + prima)

