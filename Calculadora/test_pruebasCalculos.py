import logicaLiquidacion
import unittest
from datetime import datetime

class testCalculoLiquidacion(unittest.TestCase):
    
    def test_fecha_normal(self):
        fecha_inicio_str = "01/01/2006"
        fecha_fin_str = "31/01/2006"

        diferencia = logicaLiquidacion.calculo_tiempo_trabajado_dias(fecha_inicio_str, fecha_fin_str)

        self.assertEqual(diferencia, 30)

    def test_caso_normal1(self):
        fecha_inicio_str = "01/01/2026"
        fecha_fin_str = "31/12/2026"

        diferencia = logicaLiquidacion.calculo_tiempo_trabajado_dias(fecha_inicio_str, fecha_fin_str)
        
        salario = 1_750_905

        cesantias = logicaLiquidacion.calculo_cesantias(salario, diferencia)
        interescCesantias = logicaLiquidacion.calculo_interes_cesantias(salario, diferencia)
        vacaciones = logicaLiquidacion.calculo_vacaciones(salario, diferencia)
        primaServicios = logicaLiquidacion.calculo_prima_servicios(salario, diferencia)
        pagoNeto = logicaLiquidacion. calculo_pago_neto(cesantias, interescCesantias, vacaciones, primaServicios)

        self.assertEqual(diferencia, 360)
        self.assertEqual(pagoNeto, 4587371)

    def test_caso_normal2(self):
        fecha_inicio_str = "01/01/2026"
        fecha_fin_str = "01/06/2026"

        diferencia = logicaLiquidacion.calculo_tiempo_trabajado_dias(fecha_inicio_str, fecha_fin_str)
        
        salario = 3_501_810

        cesantias = logicaLiquidacion.calculo_cesantias(salario, diferencia)
        interescCesantias = logicaLiquidacion.calculo_interes_cesantias(cesantias, diferencia)
        vacaciones = logicaLiquidacion.calculo_vacaciones(salario, diferencia)
        primaServicios = logicaLiquidacion.calculo_prima_servicios(salario, diferencia)
        pagoNeto = logicaLiquidacion. calculo_pago_neto(cesantias, interescCesantias, vacaciones, primaServicios)

        self.assertEqual(diferencia, 150)
        self.assertAlmostEqual(pagoNeto, 3720673,0)

    def test_caso_normal3(self):
        fecha_inicio_str = "01/08/2026"
        fecha_fin_str = "31/08/2026"

        diferencia = logicaLiquidacion.calculo_tiempo_trabajado_dias(fecha_inicio_str, fecha_fin_str)
        
        salario = 5_050_000

        cesantias = logicaLiquidacion.calculo_cesantias(salario, diferencia)
        interescCesantias = logicaLiquidacion.calculo_interes_cesantias(cesantias, diferencia)
        vacaciones = logicaLiquidacion.calculo_vacaciones(salario, diferencia)
        primaServicios = logicaLiquidacion.calculo_prima_servicios(salario, diferencia)
        pagoNeto = logicaLiquidacion. calculo_pago_neto(cesantias, interescCesantias, vacaciones, primaServicios)

        self.assertEqual(diferencia, 30)
        self.assertAlmostEqual(pagoNeto, 1056292)
    
    def test_contrato_corto(self):
        fecha_inicio_str = "10/01/2026"
        fecha_fin_str = "20/01/2026"

        diferencia = logicaLiquidacion.calculo_tiempo_trabajado_dias(fecha_inicio_str, fecha_fin_str)
        
        salario = 6_000_000

        cesantias = logicaLiquidacion.calculo_cesantias(salario, diferencia)
        interescCesantias = logicaLiquidacion.calculo_interes_cesantias(cesantias, diferencia)
        vacaciones = logicaLiquidacion.calculo_vacaciones(salario, diferencia)
        primaServicios = logicaLiquidacion.calculo_prima_servicios(salario, diferencia)
        pagoNeto = logicaLiquidacion. calculo_pago_neto(cesantias, interescCesantias, vacaciones, primaServicios)

        self.assertEqual(diferencia, 10)
        self.assertEqual(pagoNeto, 417222)

    def test_cambio_semestre(self):
        fecha_inicio_str = "01/06/2026"
        fecha_fin_str = "01/08/2026"

        diferencia = logicaLiquidacion.calculo_tiempo_trabajado_dias(fecha_inicio_str, fecha_fin_str)
        
        salario = 1_750_905

        cesantias = logicaLiquidacion.calculo_cesantias(salario, diferencia)
        interescCesantias = logicaLiquidacion.calculo_interes_cesantias(cesantias, diferencia)
        vacaciones = logicaLiquidacion.calculo_vacaciones(salario, diferencia)
        primaServicios = logicaLiquidacion.calculo_prima_servicios(salario, diferencia)
        pagoNeto = logicaLiquidacion. calculo_pago_neto(cesantias, interescCesantias, vacaciones, primaServicios)

        self.assertEqual(diferencia, 60)
        self.assertEqual(pagoNeto, 735380)

    def test_salario_menor_SMMLV(self):
        fecha_inicio_str = "06/09/2026"
        fecha_fin_str = "31/10/2026"

        diferencia = logicaLiquidacion.calculo_tiempo_trabajado_dias(fecha_inicio_str, fecha_fin_str)
        
        salario = 1_600_000

        cesantias = logicaLiquidacion.calculo_cesantias(salario, diferencia)
        interescCesantias = logicaLiquidacion.calculo_interes_cesantias(cesantias, diferencia)
        vacaciones = logicaLiquidacion.calculo_vacaciones(salario, diferencia)
        primaServicios = logicaLiquidacion.calculo_prima_servicios(salario, diferencia)
        pagoNeto = logicaLiquidacion. calculo_pago_neto(cesantias, interescCesantias, vacaciones, primaServicios)

        self.assertEqual(diferencia, 55)
        self.assertEqual(pagoNeto, 615593)
    
    def test_salario_menorigual_cero(self):
        with self.assertRaises(logicaLiquidacion.ErrorSalario):
            logicaLiquidacion.validar_salario(0)
        
    def test_fecha_retiro_anterior_a_fecha_ingreso(self):
        with self.assertRaises(logicaLiquidacion.ErrorFecha):
            logicaLiquidacion.calculo_tiempo_trabajado_dias("10/04/2026", "28/03/2026")

    def test_fecha_ingresada_inexistente(self):
        with self.assertRaises(ValueError):
            logicaLiquidacion.calculo_tiempo_trabajado_dias("32/04/2026", "01/05/2026")

    def test_fecha_formato_invalida(self):
        with self.assertRaises(ValueError):
            logicaLiquidacion.calculo_tiempo_trabajado_dias("cualquiera", "05/14/2026")
    
    def test_valor_ingresado_en_formato_invalivo(self):
        with self.assertRaises(logicaLiquidacion.ErrorSalario):
            logicaLiquidacion.validar_salario("Tres Millones")
        
if __name__ == "__main__":
    unittest.main()