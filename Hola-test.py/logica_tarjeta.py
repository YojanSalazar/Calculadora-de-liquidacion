

def calcular_cuota(compra, interes, plazo):
    """
    :compra: Valor de la compra con la tarjeta
    :interes: Tasa de interes mensual representada como decimal
    :plazo: Numero de cuoatas a diferir la compra
    """
    
    return (compra * interes)/(1-((1+interes)**(-plazo))) 