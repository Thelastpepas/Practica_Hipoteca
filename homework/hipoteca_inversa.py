
# Excepciones 

class ErrorTipoDato(Exception):
    pass

class ErrorValorInmueble(Exception):
    pass

class ErrorEdadInvalida(Exception):
    pass

class ErrorTasaInteres(Exception):
    pass

class ErrorEstadoInmueble(Exception):
    pass

class ErrorEstadoCivil(Exception):
    pass

class ErrorValorInmuebleBajo(Exception):
    pass

class ErrorValorInmuebleAlto(Exception):
    pass


def calcularCuotaHipotecaInversa(valor_inmueble, estado_inmueble, estado_civil, edad_propietario, edad_conyuge, tasa_interes):
    # Verificación de tipos de datos
    if not isinstance(valor_inmueble, (int, float)) or not isinstance(edad_propietario, int) or not isinstance(edad_conyuge, int) or not isinstance (tasa_interes,(int,float)):
        raise ErrorTipoDato("Tipo de dato incorrecto")

    if valor_inmueble < 200000000:
        raise ErrorValorInmuebleBajo("El valor del inmueble es demasiado bajo, debe ser mayor o igual a 200 millones")

    if valor_inmueble > 900000000:
        raise ErrorValorInmuebleAlto("El valor del inmueble es demasiado alto, debe ser menor o igual a 900 millones")
    # Verificación de valores
    if valor_inmueble <= 0:
        raise ErrorValorInmueble("El valor del inmueble debe ser mayor que cero")

    if edad_propietario < 18 or edad_conyuge < 18 :
        raise ErrorEdadInvalida("debe ser mayoy de edad ")
    edad_minima= min(edad_conyuge,edad_propietario)    
    if edad_minima >85 :
        raise ErrorEdadInvalida("Supero el limite de edad")

    # verificación de tasa de interés igual a 0
    if tasa_interes == 0:
        raise ErrorTasaInteres("Tasa de interés no puede ser 0")
    
    if tasa_interes < 0 :
        raise ErrorTasaInteres("Tasa de interés inválida")
    
    if  tasa_interes > 1 :
        raise ErrorTasaInteres("Tasa de interés  no puede ser mayoy que 1")
    

    # Verificación de estado del inmueble
    estados_validos = ["excelente", "bueno", "regular"]
    if estado_inmueble not in estados_validos:
        raise ErrorEstadoInmueble("Estado del inmueble desconocido")

    # Verificación de estado civil
    estados_civiles_validos = ["casado", "soltero", "divorciado"]
    if estado_civil not in estados_civiles_validos:
        raise ErrorEstadoCivil("Estado civil inválido")

    pass
