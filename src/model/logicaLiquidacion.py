from datetime import datetime
from model import errores 

def validar_salario(salario):
    """
        salario: Salario ingresado por el usuario, debe ser un entero positivo.
    Raises:
        errores.ErrorSalarioNoEntero: Cuando el salario ingresado no es un número entero.
        errores.ErrorSalarioMenorDeCero: Cuando el salario ingresado es menor o igual a cero.
    Returns:
        bool: True si el salario es válido.
    """
    if not isinstance(salario, int):
        raise errores.ErrorSalarioNoEntero()
    if salario <= 0:
        raise errores.ErrorSalarioMenorDeCero()
    return True
    
formato_fecha = "%d/%m/%Y"

def convertir_fecha(fecha):
    """
        fecha: Fecha ingresada por el usuario en formato "DD/MM/AAAA". 
    Raises:
        errores.ErrorFechaFormatoIncorrecto: Cuando la fecha ingresada no cumple con el formato esperado o es inválida.
    Returns:
        datetime: Transformación de la cadena de texto a un objeto datetime.
    """
    if not fecha:
        raise errores.ErrorFechaFormatoIncorrecto()
    try:
        return datetime.strptime(fecha, formato_fecha)
    except ValueError:
        raise errores.ErrorFechaFormatoIncorrecto()
    
def validar_rango_fechas(inicio, fin):
    """
        inicio: agarra la fecha de inicio convertida a datetime.
        fin: agarra la fecha de fin convertida a datetime.
    Raises:
        errores.ErrorFechaIncorrecta: Cuando la fecha de fin es anterior a la fecha de inicio.
    """
    if fin < inicio: 
        raise errores.ErrorFechaIncorrecta()
    
def calcular_dias_360(fecha_inicio, fecha_fin):
    """
        fecha_inicio: Fecha de inicio.
        fecha_fin: Fecha de fin.

    Returns:
        int: Número de días en el rango de fechas utilizando el método 360.
    """
    y1, m1, d1 = fecha_inicio.year, fecha_inicio.month, fecha_inicio.day
    y2, m2, d2 = fecha_fin.year, fecha_fin.month, fecha_fin.day

    return (y2 - y1) * 360 + (m2 - m1) * 30 + (d2 - d1)

def calcular_tiempo_trabajado_dias(inicio, fin):
    """
        inicio: Fecha de inicio en formato "DD/MM/AAAA".
        fin: Fecha de fin en formato "DD/MM/AAAA".
        
    Returns:
        int: Número de días en el rango de fechas utilizando el método 360
    """
    fecha_inicio = convertir_fecha(inicio)
    fecha_fin = convertir_fecha(fin)
    
    validar_rango_fechas(fecha_inicio, fecha_fin)
    
    return calcular_dias_360(fecha_inicio, fecha_fin)

def calcular_cesantias(salario, dias):
    """
        salario: Salario mensual del empleado ingresado, debe ser un entero positivo.
        dias: Número de días de trabajo calculados utilizando el método 360.
    Returns:
        float: Valor de las cesantías calculadas.
    """
    return (salario*dias)/360
    
def calcular_interes_cesantias(cesantias, dias):
    """
        cesantias: Valor de las cesantías calculadas.
        dias: Número de días de trabajo calculados utilizando el método 360.

    Returns:
        float: Valor de los intereses de cesantías calculados.
    """
    return (cesantias*dias*0.12)/360

def calcular_vacaciones(salario,dias):
    """
        salario: Salario mensual del empleado ingresado, debe ser un entero positivo.
        dias: Número de días de trabajo calculados utilizando el método 360.

    Returns:
        float: Valor de las vacaciones calculadas.
    """
    return(salario*dias)/720

def calcular_prima_servicios(salario, dias):
    """
        salario: Salario mensual del empleado ingresado, debe ser un entero positivo.
        dias: Número de días de trabajo calculados utilizando el método 360.
    Returns:
        float: Valor de la prima de servicios calculada.
    """
    return(salario*dias)/360

def calcular_pago_neto(cesantias, interesCesantia, vacaciones, prima):
    """
        cesantias: Valor de las cesantías calculadas.
        interesCesantia: Valor de los intereses de cesantías calculados.
        vacaciones: Valor de las vacaciones calculadas.
        prima: Valor de la prima de servicios calculada.

    Returns:
        float: Valor total de la liquidación calculada sumando cesantías, intereses de cesantías, vacaciones y prima de servicios.
    """
    return round(cesantias + interesCesantia + vacaciones + prima)

