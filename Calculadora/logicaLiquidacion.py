from datetime import datetime


def validar_salario(salario):
    if not isinstance(salario, int):
        raise ErrorSalario("Debe ingresar valores correctos.")
    if salario <= 0:
        raise ErrorSalario("El salario debe ser mayor a 0.")


def calculo_tiempo_trabajado_dias(inicio, fin):
    formato = "%d/%m/%Y"

    fecha_inicio = datetime.strptime(inicio, formato)
    fecha_fin = datetime.strptime(fin, formato)

    if fecha_fin < fecha_inicio:
        raise ErrorFecha("La fecha de retiro no puede ser anterior.")

    y1, m1, d1 = fecha_inicio.year, fecha_inicio.month, fecha_inicio.day
    y2, m2, d2 = fecha_fin.year, fecha_fin.month, fecha_fin.day

    return (y2 - y1) * 360 + (m2 - m1) * 30 + (d2 - d1)


def calculo_cesantias(salario, dias):
    return (salario*dias)/360
    
def calculo_interes_cesantias(cesantias, dias):
    return (cesantias*dias*0.12)/360

def calculo_vacaciones(salario,dias):
    return(salario*dias)/720

def calculo_prima_servicios(salario, dias):
    return(salario*dias)/360

def calculo_pago_neto(cesantias, interesCesantia, vacaciones, prima):
    return round(cesantias + interesCesantia + vacaciones + prima)

class ErrorSalario(Exception):
    """Se usa cuando el valor del salario es erroneo."""

class ErrorFecha(Exception):
    """Se usa cuando el formato de la fecha está mal intoducida"""
    """Se usa también cuando se ingresa una fecha de retiro anterior a la de ingreso."""