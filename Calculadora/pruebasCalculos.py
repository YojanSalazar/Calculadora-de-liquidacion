import logicaLiquidacion
import unittest
from datetime import datetime

class testCalculoLiquidacion(unittest.TestCase):
    
    def test_fecha_normal(self):
        formato = "%d/%m/%Y"
        fecha_inicio_str = "01/01/2006"
        fecha_fin_str = "31/01/2006"

        fecha_inicio = datetime.strptime(fecha_inicio_str, formato).date()
        fecha_fin = datetime.strptime(fecha_fin_str, formato).date()

        y1, m1, d1 = fecha_inicio.year, fecha_inicio.month, fecha_inicio.day
        y2, m2, d2 = fecha_fin.year, fecha_fin.month, fecha_fin.day
        diferencia = (y2 - y1) * 360 + (m2 - m1) * 30 + (d2 - d1)

        self.assertEqual(diferencia, 30)

    def test_caso_normal1(self):
        formato = "%d/%m/%Y"
        fecha_inicio_str = "01/01/2026"
        fecha_fin_str = "31/12/2026"

        fecha_inicio = datetime.strptime(fecha_inicio_str, formato)
        fecha_fin = datetime.strptime(fecha_fin_str, formato)

        y1, m1, d1 = fecha_inicio.year, fecha_inicio.month, fecha_inicio.day
        y2, m2, d2 = fecha_fin.year, fecha_fin.month, fecha_fin.day
        diferencia = (y2 - y1) * 360 + (m2 - m1) * 30 + (d2 - d1)
        salario = 1_750_905

        cesantias = logicaLiquidacion.calculo_cesantias(salario, diferencia)
        interescCesantias = logicaLiquidacion.calculo_interes_cesantias(salario, diferencia)
        vacaciones = logicaLiquidacion.calculo_vacaciones(salario, diferencia)
        primaServicios = logicaLiquidacion.calculo_prima_servicios(salario, diferencia)
        pagoNeto = logicaLiquidacion. calculo_pago_neto(cesantias, interescCesantias, vacaciones, primaServicios)

        self.assertEqual(diferencia, 360)
        self.assertEqual(pagoNeto, 4587371)

    def test_caso_normal2(self):
        formato = "%d/%m/%Y"
        fecha_inicio_str = "01/01/2026"
        fecha_fin_str = "01/06/2026"

        fecha_inicio = datetime.strptime(fecha_inicio_str, formato)
        fecha_fin = datetime.strptime(fecha_fin_str, formato)

        y1, m1, d1 = fecha_inicio.year, fecha_inicio.month, fecha_inicio.day
        y2, m2, d2 = fecha_fin.year, fecha_fin.month, fecha_fin.day
        diferencia = (y2 - y1) * 360 + (m2 - m1) * 30 + (d2 - d1)
        salario = 3_501_810

        cesantias = logicaLiquidacion.calculo_cesantias(salario, diferencia)
        interescCesantias = logicaLiquidacion.calculo_interes_cesantias(cesantias, diferencia)
        vacaciones = logicaLiquidacion.calculo_vacaciones(salario, diferencia)
        primaServicios = logicaLiquidacion.calculo_prima_servicios(salario, diferencia)
        pagoNeto = logicaLiquidacion. calculo_pago_neto(cesantias, interescCesantias, vacaciones, primaServicios)

        self.assertEqual(diferencia, 150)
        self.assertAlmostEqual(pagoNeto, 3720673,0)

    def test_caso_normal3(self):
        formato = "%d/%m/%Y"
        fecha_inicio_str = "01/08/2026"
        fecha_fin_str = "31/08/2026"

        fecha_inicio = datetime.strptime(fecha_inicio_str, formato)
        fecha_fin = datetime.strptime(fecha_fin_str, formato)

        y1, m1, d1 = fecha_inicio.year, fecha_inicio.month, fecha_inicio.day
        y2, m2, d2 = fecha_fin.year, fecha_fin.month, fecha_fin.day
        diferencia = (y2 - y1) * 360 + (m2 - m1) * 30 + (d2 - d1)
        salario = 5_050_000

        cesantias = logicaLiquidacion.calculo_cesantias(salario, diferencia)
        interescCesantias = logicaLiquidacion.calculo_interes_cesantias(cesantias, diferencia)
        vacaciones = logicaLiquidacion.calculo_vacaciones(salario, diferencia)
        primaServicios = logicaLiquidacion.calculo_prima_servicios(salario, diferencia)
        pagoNeto = logicaLiquidacion. calculo_pago_neto(cesantias, interescCesantias, vacaciones, primaServicios)

        self.assertEqual(diferencia, 30)
        self.assertAlmostEqual(pagoNeto, 1056292)
    
    def test_contrato_corto(self):
        formato = "%d/%m/%Y"
        fecha_inicio_str = "10/01/2026"
        fecha_fin_str = "20/01/2026"

        fecha_inicio = datetime.strptime(fecha_inicio_str, formato)
        fecha_fin = datetime.strptime(fecha_fin_str, formato)

        y1, m1, d1 = fecha_inicio.year, fecha_inicio.month, fecha_inicio.day
        y2, m2, d2 = fecha_fin.year, fecha_fin.month, fecha_fin.day
        diferencia = (y2 - y1) * 360 + (m2 - m1) * 30 + (d2 - d1)

        salario = 6_000_000
        cesantias = logicaLiquidacion.calculo_cesantias(salario, diferencia)
        interescCesantias = logicaLiquidacion.calculo_interes_cesantias(cesantias, diferencia)
        vacaciones = logicaLiquidacion.calculo_vacaciones(salario, diferencia)
        primaServicios = logicaLiquidacion.calculo_prima_servicios(salario, diferencia)
        pagoNeto = logicaLiquidacion. calculo_pago_neto(cesantias, interescCesantias, vacaciones, primaServicios)

        self.assertEqual(diferencia, 10)
        self.assertEqual(pagoNeto, 417222)

    def test_cambio_semestre(self):
        formato = "%d/%m/%Y"
        fecha_inicio_str = "01/06/2026"
        fecha_fin_str = "01/08/2026"

        fecha_inicio = datetime.strptime(fecha_inicio_str, formato)
        fecha_fin = datetime.strptime(fecha_fin_str, formato)

        y1, m1, d1 = fecha_inicio.year, fecha_inicio.month, fecha_inicio.day
        y2, m2, d2 = fecha_fin.year, fecha_fin.month, fecha_fin.day
        diferencia = (y2 - y1) * 360 + (m2 - m1) * 30 + (d2 - d1)

        salario = 1_750_905
        cesantias = logicaLiquidacion.calculo_cesantias(salario, diferencia)
        interescCesantias = logicaLiquidacion.calculo_interes_cesantias(cesantias, diferencia)
        vacaciones = logicaLiquidacion.calculo_vacaciones(salario, diferencia)
        primaServicios = logicaLiquidacion.calculo_prima_servicios(salario, diferencia)
        pagoNeto = logicaLiquidacion. calculo_pago_neto(cesantias, interescCesantias, vacaciones, primaServicios)

        self.assertEqual(diferencia, 60)
        self.assertEqual(pagoNeto, 735380)

    def test_salario_menor_SMMLV(self):
        formato = "%d/%m/%Y"
        fecha_inicio_str = "06/09/2026"
        fecha_fin_str = "31/10/2026"

        fecha_inicio = datetime.strptime(fecha_inicio_str, formato)
        fecha_fin = datetime.strptime(fecha_fin_str, formato)

        y1, m1, d1 = fecha_inicio.year, fecha_inicio.month, fecha_inicio.day
        y2, m2, d2 = fecha_fin.year, fecha_fin.month, fecha_fin.day
        diferencia = (y2 - y1) * 360 + (m2 - m1) * 30 + (d2 - d1)

        salario = 1_600_000
        cesantias = logicaLiquidacion.calculo_cesantias(salario, diferencia)
        interescCesantias = logicaLiquidacion.calculo_interes_cesantias(cesantias, diferencia)
        vacaciones = logicaLiquidacion.calculo_vacaciones(salario, diferencia)
        primaServicios = logicaLiquidacion.calculo_prima_servicios(salario, diferencia)
        pagoNeto = logicaLiquidacion. calculo_pago_neto(cesantias, interescCesantias, vacaciones, primaServicios)

        self.assertEqual(diferencia, 55)
        self.assertEqual(pagoNeto, 615593)
    
    def test_salario_menorigual_cero(self):
        with self.assertRaises(ValueError):
            logicaLiquidacion.validar_salario(0)
        

unittest.main()