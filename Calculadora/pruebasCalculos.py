import calculosLiquidacion
import unittest
from datetime import datetime

class testCalculoLiquidacion(unittest.TestCase):
    
    def test_fecha_normal(self):
        formato = "%d/%m/%Y"
        fecha_inicio_str = "25/08/2006"
        fecha_fin_str = "25/08/2007"

        fecha_inicio = datetime.strptime(fecha_inicio_str, formato)
        fecha_fin = datetime.strptime(fecha_fin_str, formato)

        diferencia = abs((fecha_fin - fecha_inicio).days)

        self.assertEqual(diferencia, 365)

unittest.main()