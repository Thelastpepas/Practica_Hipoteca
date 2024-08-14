import unittest
import hipoteca_inversa

class HipotecaInversaTest(unittest.TestCase):

    # Casos de Error

    def test_Error_1(self):
        valor_inmueble = ""
        estado_inmueble = "excelente"
        estado_civil = "casado"
        edad_propietario = 70
        edad_conyuge = 68
        tasa_interes = 0.07
        with self.assertRaises(hipoteca_inversa.ErrorTipoDato):
            hipoteca_inversa.calcularCuotaHipotecaInversa(valor_inmueble, estado_inmueble, estado_civil, edad_propietario, edad_conyuge, tasa_interes)

    def test_Error_2(self):
        valor_inmueble = 0  # valor inmueble 0
        estado_inmueble = "excelente"
        estado_civil = "casado"
        edad_propietario = 70  
        edad_conyuge = 68
        tasa_interes = 0.07
        with self.assertRaises(hipoteca_inversa.ErrorValorInmueble):
            hipoteca_inversa.calcularCuotaHipotecaInversa(valor_inmueble, estado_inmueble, estado_civil, edad_propietario, edad_conyuge, tasa_interes)

    def test_Error_3(self):
        valor_inmueble = -300000000  # valor de inmueble negativo
        estado_inmueble = "excelente"
        estado_civil = "casado"
        edad_propietario = 70
        edad_conyuge = 68
        tasa_interes = 0.07
        with self.assertRaises(hipoteca_inversa.ErrorValorInmueble):
            hipoteca_inversa.calcularCuotaHipotecaInversa(valor_inmueble, estado_inmueble, estado_civil, edad_propietario, edad_conyuge, tasa_interes)

    def test_Error_4(self):
        valor_inmueble = 400000000
        estado_inmueble = "excelente"
        estado_civil = "casado"
        edad_propietario = 70
        edad_conyuge = 68
        tasa_interes = 0  # Tasa de interés es 0
        with self.assertRaises(hipoteca_inversa.ErrorTasaInteres):
            hipoteca_inversa.calcularCuotaHipotecaInversa(valor_inmueble, estado_inmueble, estado_civil, edad_propietario, edad_conyuge, tasa_interes)

    def test_Error_5(self):
        valor_inmueble = 300000000
        estado_inmueble = "desconocido"  # Estado inválido
        estado_civil = "casado"
        edad_propietario = 70
        edad_conyuge = 68
        tasa_interes = 0.07
        with self.assertRaises(hipoteca_inversa.ErrorEstadoInmueble):
            hipoteca_inversa.calcularCuotaHipotecaInversa(valor_inmueble, estado_inmueble, estado_civil, edad_propietario, edad_conyuge, tasa_interes)

    def test_Error_6(self):
        valor_inmueble = 200000000
        estado_inmueble = "excelente"
        estado_civil = "casado"
        edad_propietario = ""
        edad_conyuge = 68
        tasa_interes = 0.07
        with self.assertRaises(hipoteca_inversa.ErrorTipoDato):
            hipoteca_inversa.calcularCuotaHipotecaInversa(valor_inmueble, estado_inmueble, estado_civil, edad_propietario, edad_conyuge, tasa_interes)

    def test_Error_7(self):
        valor_inmueble = "300000000p"
        estado_inmueble = "bueno"  
        estado_civil = "casado"
        edad_propietario = 70
        edad_conyuge = 68
        tasa_interes = 0.07
        with self.assertRaises(hipoteca_inversa.ErrorTipoDato):
            hipoteca_inversa.calcularCuotaHipotecaInversa(valor_inmueble, estado_inmueble, estado_civil, edad_propietario, edad_conyuge, tasa_interes)

    def test_Error_8(self):
        valor_inmueble = 300000000
        estado_inmueble = "excelente"
        estado_civil = None  # Estado civil nulo
        edad_propietario = 70
        edad_conyuge = 68
        tasa_interes = 0.07
        with self.assertRaises(hipoteca_inversa.ErrorEstadoCivil):
            hipoteca_inversa.calcularCuotaHipotecaInversa(valor_inmueble, estado_inmueble, estado_civil, edad_propietario, edad_conyuge, tasa_interes)

if __name__ == '__main__':
    unittest.main()
