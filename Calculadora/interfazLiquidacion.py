import logicaLiquidacion
from datetime import datetime

def calculo_tiempo_trabajado_dias():
    try:
        fecha_inicio = input("Fecha ingreso (DD/MM/AAAA): ")
        fecha_fin = input("Fecha retiro (DD/MM/AAAA): ")

        dias= logicaLiquidacion.calculo_tiempo_trabajado_dias(fecha_inicio, fecha_fin)
        
        print(f'Dias trabajados: {dias}')

    except:
        raise ValueError("El formato de la fecha está incorrecto.")

calculo_tiempo_trabajado_dias()