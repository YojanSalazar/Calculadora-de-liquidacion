import logicaLiquidacion
from datetime import datetime

def ingreso_fechas():
    
        fecha_inicio = input("Fecha ingreso (DD/MM/AAAA): ")
        fecha_fin = input("Fecha retiro (DD/MM/AAAA): ")

        dias = logicaLiquidacion.calculo_tiempo_trabajado_dias(fecha_inicio, fecha_fin)

def ingreso_salario():
    salario = input("Ingrese su SMMLV: ")
    logicaLiquidacion.validar_salario(salario)
    
ingreso_fechas()