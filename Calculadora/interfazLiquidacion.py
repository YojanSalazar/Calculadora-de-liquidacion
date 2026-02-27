import logicaLiquidacion
from datetime import datetime

def ingreso_fechas():
    
        fecha_inicio = input("Fecha ingreso (DD/MM/AAAA): ")
        fecha_fin = input("Fecha retiro (DD/MM/AAAA): ")

        dias = logicaLiquidacion.calculo_tiempo_trabajado_dias(fecha_inicio, fecha_fin)

def ingreso_salario():
    salariominimo = input("SMMLV: ")
    print(isinstance(salariominimo, str))
    logicaLiquidacion.validar_salario(salariominimo)
    
    

while True:
    print("\nBienvenido al programa para calcular la liquidación de su ex-empleado.")
    print("---------------------------------------------------------------------")
    print("Ingrese la fecha de inicio y final del contrato.")
    #ingreso_fechas()
    print("Ingrese el salario.")
    ingreso_salario()