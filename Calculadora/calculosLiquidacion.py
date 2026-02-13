from datetime import datetime

def calculo_tiempo_trabajado_dias():
    formato = "%d/%m/%Y"
    try:
        fecha_inicio_str = input("Introduce la fecha de ingreso (DD/MM/AAAA): ")
        fecha_fin_str = input("Introduce la fecha de retiro (DD/MM/AAAA): ")

        fecha_inicio = datetime.strptime(fecha_inicio_str, formato)
        fecha_fin = datetime.strptime(fecha_fin_str, formato)

        diferencia = abs((fecha_fin - fecha_inicio).days)

        return diferencia
    
    except ValueError:
        print("Error: El formato de fecha es incorrecto. Usa DD/MM/AAAA (ej: 15/05/2024).")


def calculo_cesantias():
    ...

def calculo_interes_cesantias():
    ...

def calculo_vacaciones():
    ...

def calculo_prima_servicios():
    ...

def calculo_pago_neto():
    ...
