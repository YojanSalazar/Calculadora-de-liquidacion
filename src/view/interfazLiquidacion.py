import sys
sys.path.append("src")

from model import logicaLiquidacion
from datetime import datetime

def ingreso_fechas():
    fecha_inicio = input("Fecha ingreso (DD/MM/AAAA): ")
    fecha_fin = input("Fecha retiro (DD/MM/AAAA): ")

    return logicaLiquidacion.calcular_tiempo_trabajado_dias(fecha_inicio, fecha_fin)

def ingreso_salario():
    salariominimo = input("SMMLV: ")
    salariominimo = int(salariominimo)
    valido = logicaLiquidacion.validar_salario(salariominimo)
    if valido:
        return salariominimo

print("\nBienvenido al programa para calcular la liquidación de su ex-empleado.")
print("---------------------------------------------------------------------")
print("Ingrese la fecha de inicio y final del contrato.")
dias = ingreso_fechas()
print("Ingrese el salario.")
salario = ingreso_salario() 

while True:
    
    print("\n¿Qué desea hacer?")
    print("1. Calcular liquidación")
    print("2. Visualizar dias trabajados")
    print("3. Visualizar cesantias")
    print("4. Visualizar intereses de cesantias")
    print("5. Visualizar vacaciones")
    print("6. Visualizar prima de servicios")
    print("0. Salir")

    opcion = input("Ingrese el número de la opción deseada: ")

    if opcion == "1":
        cesantias = logicaLiquidacion.calcular_cesantias(salario, dias)
        interesCesantia = logicaLiquidacion.calcular_interes_cesantias(cesantias, dias)
        vacaciones = logicaLiquidacion.calcular_vacaciones(salario, dias)
        prima = logicaLiquidacion.calcular_prima_servicios(salario, dias)
        pago_neto = logicaLiquidacion.calcular_pago_neto(cesantias, interesCesantia, vacaciones, prima)
        print(f"\nEl valor total de la liquidación es: {pago_neto}")
    elif opcion == "2":
        print(f"\nEl número de días trabajados es: {dias}")
    elif opcion == "3":
        cesantias = logicaLiquidacion.calcular_cesantias(salario, dias)
        print(f"\nEl valor de las cesantías es: {cesantias}")
    elif opcion == "4":
        cesantias = logicaLiquidacion.calcular_cesantias(salario, dias)
        interesCesantia = logicaLiquidacion.calcular_interes_cesantias(cesantias, dias)
        print(f"\nEl valor de los intereses de cesantías es: {interesCesantia}")
    elif opcion == "5":
        vacaciones = logicaLiquidacion.calcular_vacaciones(salario, dias)
        print(f"\nEl valor de las vacaciones es: {vacaciones}")
    elif opcion == "6":
        prima = logicaLiquidacion.calcular_prima_servicios(salario, dias)
        print(f"\nEl valor de la prima de servicios es: {prima}")
    elif opcion == "0":
        print("\nGracias por usar el programa. ¡Hasta luego!")
        break
    else:
        print("\nOpción no válida. Por favor, ingrese un número del 0 al 6.")