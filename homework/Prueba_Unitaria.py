import unittest
import hipoteca_inversa

class HipotecaInversaTest(unittest.TestCase):

    # Casos Normales

    def test_Normal_1(self):
        # variables de entradas
        valor_inmueble = 500000000
        estado_inmueble = "excelente"
        estado_civil = "casado"
        edad_propietario = 70
        edad_conyuge = 68
        tasa_interes = 0.5
        #variables de salida
        cuota_esperada = 1041666.667
        resultado = hipoteca_inversa.calcularCuotaHipotecaInversa(valor_inmueble, estado_inmueble, estado_civil, edad_propietario, edad_conyuge, tasa_interes)
        self.assertEqual(round(resultado, 2), cuota_esperada)

    def test_Normal_2(self):
         # variables de entradas
        valor_inmueble = 400000000
        estado_inmueble = "bueno"
        estado_civil = "casado"
        edad_propietario = 72
        edad_conyuge = 70
        tasa_interes = 0.5
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
        valor_inmueble = 300000000
        estado_inmueble = "regular"
        estado_civil = "casado"
        edad_propietario = 70
        edad_conyuge = 68
        tasa_interes = 0.5
        #variables de salida
        cuota_esperada = 500000
        resultado = hipoteca_inversa.calcularCuotaHipotecaInversa(valor_inmueble, estado_inmueble, estado_civil, edad_propietario, edad_conyuge, tasa_interes)
        self.assertEqual(round(resultado, 2), cuota_esperada)

    def test_Normal_5(self):
         # variables de entradas
        valor_inmueble = 350000000
        estado_inmueble = "excelente"
        estado_civil = "casado"
        edad_propietario = 75
        edad_conyuge = 65 
        tasa_interes = 0.06
        #variables de salida
        cuota_esperada = 625000
        resultado = hipoteca_inversa.calcularCuotaHipotecaInversa(valor_inmueble, estado_inmueble, estado_civil, edad_propietario, edad_conyuge, tasa_interes)
        self.assertEqual(round(resultado, 2), cuota_esperada)

    def test_Normal_6(self):
         # variables de entradas
        valor_inmueble = 280000000
        estado_inmueble = "bueno"
        estado_civil = "casado"
        edad_propietario = 80
        edad_conyuge = 70 
        tasa_interes = 0.08
        #variables de salida
        cuota_esperada = 700000
        resultado = hipoteca_inversa.calcularCuotaHipotecaInversa(valor_inmueble, estado_inmueble, estado_civil, edad_propietario, edad_conyuge, tasa_interes)
        self.assertEqual(round(resultado, 2), cuota_esperada)

    # Casos Extraordinarios

    def test_Extraordinario_1(self):
         # variables de entradas
        valor_inmueble =  650000000
        estado_inmueble = "bueno"
        estado_civil = "casado"
        edad_propietario = 90
        edad_conyuge = 85  # edad limite es 85 y el conyugue esta al limite
        tasa_interes = 0.05 
        #variables de salida
        cuota_esperada = 1625000

        resultado = hipoteca_inversa.calcularCuotaHipotecaInversa(valor_inmueble, estado_inmueble, estado_civil, edad_propietario, edad_conyuge, tasa_interes)
        self.assertEqual(round(resultado, 2), cuota_esperada)

    def test_Extraordinario_2(self):
         # variables de entradas
        valor_inmueble = 300000000
        estado_inmueble = "excelente"
        estado_civil = "casado"
        edad_propietario = 80  
        edad_conyuge = 18 #"Edad muy baja"  # demasiado joven para pedir una hipoteca
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
        valor_inmueble = 200000000      # valor del inmuble demasiado bajo. esta en el limite
        estado_inmueble = "excelente"
        estado_civil = " Casado"
        edad_propietario = 70
        edad_conyuge = 70  #
        tasa_interes = 0.07
        #variables de salida
        cuota_esperada = 555555.5556
        resultado = hipoteca_inversa.calcularCuotaHipotecaInversa(valor_inmueble, estado_inmueble, estado_civil, edad_propietario, max(0, edad_conyuge), tasa_interes)
        self.assertEqual(round(resultado, 2), cuota_esperada)

    def test_Extraordinario_5(self):
         # variables de entradas
        valor_inmueble = 500000000
        estado_inmueble = "bueno"
        estado_civil = "casado"
        edad_propietario = 70 #
        edad_conyuge = 85   # diferencia de edad considerable  entre el conyugue y el propietario  
        tasa_interes = 0.07
        #variables de salida
        cuota_esperada = 1250000
        resultado = hipoteca_inversa.calcularCuotaHipotecaInversa(valor_inmueble, estado_inmueble, estado_civil, min(120, edad_propietario), edad_conyuge, tasa_interes)
        self.assertEqual(round(resultado, 2), cuota_esperada)

    def test_Extraordinario_6(self):
         # variables de entradas
        valor_inmueble = 900000000  # El valor del inmuble es demasido alto y esta en el limite, ademas es regular pero aun asi tiene ese valor
        estado_inmueble = "regular"
        estado_civil = "casado"
        edad_propietario = 70
        edad_conyuge = 65  
        tasa_interes = 0.1
        #variables de salida
        cuota_esperada = 1500000
        resultado = hipoteca_inversa.calcularCuotaHipotecaInversa(valor_inmueble, estado_inmueble, estado_civil, edad_propietario, edad_conyuge, tasa_interes)
        self.assertEqual(resultado, cuota_esperada)
    
     

    # Casos de Error

    def test_Error_1(self):
            valor_inmueble = ""  # valor del inmueble desconocido
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
            valor_inmueble = 250000000
            estado_inmueble = "excelente"
            estado_civil = "casado"
            edad_propietario = ""       # edad del propetario vacia
            edad_conyuge = 68
            tasa_interes = 0.07
            with self.assertRaises(hipoteca_inversa.ErrorTipoDato):
                hipoteca_inversa.calcularCuotaHipotecaInversa(valor_inmueble, estado_inmueble, estado_civil, edad_propietario, edad_conyuge, tasa_interes)

        
    def test_Error_7(self):
            valor_inmueble = "300000000p"  #error tipo de dato
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


    def test_Error_9(self):
            valor_inmueble = 400000000
            estado_inmueble = "excelente"
            estado_civil = "casado"
            edad_propietario = 70
            edad_conyuge = 68
            tasa_interes = 2  # Tasa de interés es mayor que 5
            with self.assertRaises(hipoteca_inversa.ErrorTasaInteres):
                hipoteca_inversa.calcularCuotaHipotecaInversa(valor_inmueble, estado_inmueble, estado_civil, edad_propietario, edad_conyuge, tasa_interes)

    def test_Error_10(self):
            valor_inmueble = 950000000 # valor del inmueble supero el valor limite 
            estado_inmueble = "excelente"
            estado_civil = "casado"
            edad_propietario = 70
            edad_conyuge = 68
            tasa_interes = 6  
            with self.assertRaises(hipoteca_inversa.ErrorValorInmuebleAlto):
                hipoteca_inversa.calcularCuotaHipotecaInversa(valor_inmueble, estado_inmueble, estado_civil, edad_propietario, edad_conyuge, tasa_interes)


    def test_Error_11(self):
            valor_inmueble = 150000000  #valor del inmueble supero el valor limite  
            estado_inmueble = "bueno"
            estado_civil = "casado"
            edad_propietario = 70
            edad_conyuge = 68
            tasa_interes = 0.5
            with self.assertRaises(hipoteca_inversa.ErrorValorInmuebleBajo):
                hipoteca_inversa.calcularCuotaHipotecaInversa(valor_inmueble, estado_inmueble, estado_civil, edad_propietario, edad_conyuge, tasa_interes)

     


    if __name__ == '__main__':
        unittest.main()


