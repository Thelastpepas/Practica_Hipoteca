import unittest
import hipoteca_inversa

class HipotecaInversaTest(unittest.TestCase):

    # Casos Normales

    def test_Normal_1(self):
        # variables de entradas
        valor_inmueble = 300000000
        estado_inmueble = "excelente"
        estado_civil = "casado"
        edad_propietario = 70
        edad_conyuge = 68
        tasa_interes = 0.07
        #variables de salida
        cuota_esperada = 625000
        resultado = hipoteca_inversa.calcularCuotaHipotecaInversa(valor_inmueble, estado_inmueble, estado_civil, edad_propietario, edad_conyuge, tasa_interes)
        self.assertEqual(round(resultado, 2), cuota_esperada)

    def test_Normal_2(self):
         # variables de entradas
        valor_inmueble = 400000000
        estado_inmueble = "bueno"
        estado_civil = "casado"
        edad_propietario = 72
        edad_conyuge = 70
        tasa_interes = 0.07
        #variables de salida
        cuota_esperada = 1000000
        resultado = hipoteca_inversa.calcularCuotaHipotecaInversa(valor_inmueble, estado_inmueble, estado_civil, edad_propietario, edad_conyuge, tasa_interes)
        self.assertEqual(round(resultado, 2), cuota_esperada)

    def test_Normal_3(self):
         # variables de entradas
        valor_inmueble = 250000000
        estado_inmueble = "regular"
        estado_civil = "casado"
        edad_propietario = 65
        edad_conyuge = 67
        tasa_interes = 0.07
        #variables de salida
        cuota_esperada = 416666.6667
        resultado = hipoteca_inversa.calcularCuotaHipotecaInversa(valor_inmueble, estado_inmueble, estado_civil, edad_propietario, edad_conyuge, tasa_interes)
        self.assertEqual(round(resultado, 2), cuota_esperada)

    def test_Normal_4(self):
         # variables de entradas
        valor_inmueble = 90000000
        estado_inmueble = "regular"
        estado_civil = "casado"
        edad_propietario = 70
        edad_conyuge = 68
        tasa_interes = 0.05
        #variables de salida
        cuota_esperada = 150000
        resultado = hipoteca_inversa.calcularCuotaHipotecaInversa(valor_inmueble, estado_inmueble, estado_civil, edad_propietario, edad_conyuge, tasa_interes)
        self.assertEqual(round(resultado, 2), cuota_esperada)

    def test_Normal_5(self):
         # variables de entradas
        valor_inmueble = 100000000
        estado_inmueble = "excelente"
        estado_civil = "casado"
        edad_propietario = 75
        edad_conyuge = 65 
        tasa_interes = 0.06
        #variables de salida
        cuota_esperada = 208333.3333
        resultado = hipoteca_inversa.calcularCuotaHipotecaInversa(valor_inmueble, estado_inmueble, estado_civil, edad_propietario, edad_conyuge, tasa_interes)
        self.assertEqual(round(resultado, 2), cuota_esperada)

    def test_Normal_6(self):
         # variables de entradas
        valor_inmueble = 500000000
        estado_inmueble = "bueno"
        estado_civil = "casado"
        edad_propietario = 80
        edad_conyuge = 70 
        tasa_interes = 0.08
        #variables de salida
        cuota_esperada = 1250000
        resultado = hipoteca_inversa.calcularCuotaHipotecaInversa(valor_inmueble, estado_inmueble, estado_civil, edad_propietario, edad_conyuge, tasa_interes)
        self.assertEqual(round(resultado, 2), cuota_esperada)

    # Casos Extraordinarios

    def test_Extraordinario_1(self):
         # variables de entradas
        valor_inmueble = 100000000
        estado_inmueble = "bueno"
        estado_civil = "casado"
        edad_propietario = 99
        edad_conyuge = 98
        tasa_interes = -0.05 #tasa negativa
        #variables de salida
        cuota_esperada = 165683.5518
        resultado = hipoteca_inversa.calcularCuotaHipotecaInversa(valor_inmueble, estado_inmueble, estado_civil, edad_propietario, edad_conyuge, tasa_interes)
        self.assertEqual(round(resultado, 2), cuota_esperada)

    def test_Extraordinario_2(self):
         # variables de entradas
        valor_inmueble = 300000000
        estado_inmueble = "excelente"
        estado_civil = "casado"
        edad_propietario = 80  
        edad_conyuge = 18 #"Edad muy baja"
        tasa_interes = 0.07
        #variables de salida
        cuota_esperada = 500000
        resultado = hipoteca_inversa.calcularCuotaHipotecaInversa(valor_inmueble, estado_inmueble, estado_civil, edad_propietario, edad_conyuge, tasa_interes)
        self.assertEqual(round(resultado, 2), cuota_esperada)

    def test_Extraordinario_3(self):
         # variables de entradas
        valor_inmueble = 500000000  
        estado_inmueble = "excelente"
        estado_civil = "casado"
        edad_propietario = 70
        edad_conyuge = 68
        tasa_interes = 0.0001 #tasa de interes mu baja
        #variables de salida
        cuota_esperada = 1041666.667


        resultado = hipoteca_inversa.calcularCuotaHipotecaInversa(valor_inmueble, estado_inmueble, estado_civil, edad_propietario, edad_conyuge, tasa_interes)
        self.assertEqual(round(resultado, 2), cuota_esperada)

    def test_Extraordinario_4(self):
         # variables de entradas
        valor_inmueble = 100000000
        estado_inmueble = "excelente"
        estado_civil = "soltero"
        edad_propietario = 70
        edad_conyuge = 25  # esta soltero
        tasa_interes = 0.07
        #variables de salida
        cuota_esperada = 166666.6667
        resultado = hipoteca_inversa.calcularCuotaHipotecaInversa(valor_inmueble, estado_inmueble, estado_civil, edad_propietario, max(0, edad_conyuge), tasa_interes)
        self.assertEqual(round(resultado, 2), cuota_esperada)

    def test_Extraordinario_5(self):
         # variables de entradas
        valor_inmueble = 90000000
        estado_inmueble = "bueno"
        estado_civil = "casado"
        edad_propietario = 150  # Edad irrealmente alta
        edad_conyuge = 165  
        tasa_interes = 0.07
        #variables de salida
        cuota_esperada = 225000
        resultado = hipoteca_inversa.calcularCuotaHipotecaInversa(valor_inmueble, estado_inmueble, estado_civil, min(120, edad_propietario), edad_conyuge, tasa_interes)
        self.assertEqual(round(resultado, 2), cuota_esperada)

    def test_Extraordinario_6(self):
         # variables de entradas
        valor_inmueble = 800000000
        estado_inmueble = "regular"
        estado_civil = "casado"
        edad_propietario = 70
        edad_conyuge = 65  
        tasa_interes = 25 # tasa de interes muy alta
        #variables de salida
        cuota_esperada = 1333333.333
        resultado = hipoteca_inversa.calcularCuotaHipotecaInversa(valor_inmueble, estado_inmueble, estado_civil, edad_propietario, edad_conyuge, tasa_interes)
        self.assertEqual(resultado, cuota_esperada)

    # Casos de Error

    def test_Error_1(self):
         # variables de entradas
        valor_inmueble = ""  
        estado_inmueble = "excelente"
        estado_civil = "casado"
        edad_propietario = 70
        edad_conyuge = 68
        tasa_interes = 0.07
        #variables de salida
        cuota_esperada = "Tipo de dato incorrecto"
        resultado = hipoteca_inversa.calcularCuotaHipotecaInversa(int(valor_inmueble), estado_inmueble, estado_civil, edad_propietario, edad_conyuge, tasa_interes)
        self.assertEqual(resultado, cuota_esperada)

    def test_Error_2(self):
         # variables de entradas
        valor_inmueble = 0 # valor inmueble 0
        estado_inmueble = "excelente"
        estado_civil = "casado"
        edad_propietario = 70  
        edad_conyuge = 68
        tasa_interes = 0.07
        #variables de salida
        cuota_esperada = 0.0
        resultado = hipoteca_inversa.calcularCuotaHipotecaInversa(valor_inmueble, estado_inmueble, estado_civil, int(edad_propietario), edad_conyuge, tasa_interes)
        self.assertEqual(resultado, cuota_esperada)

    def test_Error_3(self):
         # variables de entradas
        valor_inmueble = -300000000 # valor de inmuble negativo
        estado_inmueble = "excelente"
        estado_civil = "casado"
        edad_propietario = 70
        edad_conyuge = 68
        tasa_interes = 0.07
        #variables de salida
        cuota_esperada = -1143667.126
        resultado = hipoteca_inversa.calcularCuotaHipotecaInversa(valor_inmueble, estado_inmueble, estado_civil, edad_propietario, edad_conyuge, float(tasa_interes))
        self.assertEqual(resultado, cuota_esperada)

    def test_Error_4(self):
         # variables de entradas
        valor_inmueble = 400000000
        estado_inmueble = "excelente"
        estado_civil = "casado"
        edad_propietario = 70
        edad_conyuge = 68
        tasa_interes = 0  # Tasa de interés es 0
        #variables de salida
        cuota_esperada = "No se puede dividir por cero"
        resultado = hipoteca_inversa.calcularCuotaHipotecaInversa(valor_inmueble, estado_inmueble, estado_civil, edad_propietario, edad_conyuge, tasa_interes)
        self.assertEqual(resultado, cuota_esperada)

    def test_Error_5(self):
         # variables de entradas
        valor_inmueble = 300000000
        estado_inmueble = "desconocido"  # Estado inválido
        estado_civil = "casado"
        edad_propietario = 70
        edad_conyuge = 68
        tasa_interes = 0.07
        #variables de salida
        cuota_esperada = "Estado del inmueble desconocido"
        resultado = hipoteca_inversa.calcularCuotaHipotecaInversa(valor_inmueble, estado_inmueble, estado_civil, edad_propietario, edad_conyuge, tasa_interes)
        self.assertEqual(resultado, cuota_esperada)


    def test_Error_6(self):
         # variables de entradas
        valor_inmueble = 200000000
        estado_inmueble = "excelente"
        estado_civil = "casado"
        edad_propietario = ""
        edad_conyuge = 68
        tasa_interes = 0.07
        #variables de salida
        cuota_esperada = "Edad inválida"
        resultado = hipoteca_inversa.calcularCuotaHipotecaInversa(valor_inmueble, estado_inmueble, estado_civil, max(0, edad_propietario), edad_conyuge, tasa_interes)
        self.assertEqual(resultado, cuota_esperada)

    def test_Error_7(self):
         # variables de entradas
        valor_inmueble = "300000000p"
        estado_inmueble = "bueno"  
        estado_civil = "casado"
        edad_propietario = 70
        edad_conyuge = 68
        tasa_interes = 0.07
        #variables de salida
        cuota_esperada = "tipo de dato invalido"
        resultado = hipoteca_inversa.calcularCuotaHipotecaInversa(valor_inmueble, estado_inmueble or "desconocido", estado_civil, edad_propietario, edad_conyuge, tasa_interes)
        self.assertEqual(resultado, cuota_esperada)

    def test_Error_8(self):
         # variables de entradas
        valor_inmueble = 300000000
        estado_inmueble = "excelente"
        estado_civil = None  # Estado civil nulo
        edad_propietario = 70
        edad_conyuge = 68
        tasa_interes = 0.07
        #variables de salida
        cuota_esperada = "Estado civil inválido"
        resultado = hipoteca_inversa.calcularCuotaHipotecaInversa(valor_inmueble, estado_inmueble, estado_civil or "desconocido", edad_propietario, edad_conyuge, tasa_interes)
        self.assertEqual(resultado, cuota_esperada)


if __name__ == '__main__':
    unittest.main()

