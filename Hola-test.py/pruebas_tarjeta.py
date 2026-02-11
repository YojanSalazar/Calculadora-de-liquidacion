import logica_tarjeta

def probar_caso_normal():
    #Definir datos de entrada
    compra = 200_000
    interes = 0.031
    plazo = 36

    #Realizar el proceso
    cuotaCalculada = logica_tarjeta.calcular_cuota(compra, interes, plazo)

    #Verificar las salidas  
    cuotaEsperada = 9297.96
    

    if (round(cuotaCalculada,2) == round(cuotaEsperada,2)):
        print("Prueba exitosa")
    else: 
        print("Prueba falló")

def probar_caso_normal_dos():
    #Definir datos de entrada
    compra = 850_000
    interes = 0.034
    plazo = 24

    #Realizar el proceso
    cuotaCalculada = logica_tarjeta.calcular_cuota(compra, interes, plazo)

    #Verificar las salidas  
    cuotaEsperada = 52377.50
    

    if (round(cuotaCalculada,2) == round(cuotaEsperada,2)):
        print("Prueba exitosa")
    else: 
        print("Prueba falló")

probar_caso_normal()
probar_caso_normal_dos()

