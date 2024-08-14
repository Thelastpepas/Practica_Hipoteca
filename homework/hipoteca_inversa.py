
# Excepciones personalizadas para errores en la función calcularCuotaHipotecaInversa

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


def calcularCuotaHipotecaInversa(valor_inmueble, estado_inmueble, estado_civil, edad_propietario, edad_conyuge, tasa_interes):
    # Verificación de tipos de datos
    if not isinstance(valor_inmueble, (int, float)) or not isinstance(edad_propietario, int) or not isinstance(edad_conyuge, int):
        raise ErrorTipoDato("Tipo de dato incorrecto")

    # Verificación de valores
    if valor_inmueble <= 0:
        raise ErrorValorInmueble("El valor del inmueble debe ser mayor que cero")

    if edad_propietario <= 0 or edad_conyuge <= 0 or edad_propietario > 120 or edad_conyuge > 120:
        raise ErrorEdadInvalida("Edad inválida")

    if tasa_interes < 0 or tasa_interes > 1:
        raise ErrorTasaInteres("Tasa de interés inválida")

    # Verificación de estado del inmueble
    estados_validos = ["excelente", "bueno", "regular"]
    if estado_inmueble not in estados_validos:
        raise ErrorEstadoInmueble("Estado del inmueble desconocido")

    # Verificación de estado civil
    estados_civiles_validos = ["casado", "soltero", "divorciado", "viudo"]
    if estado_civil not in estados_civiles_validos:
        raise ErrorEstadoCivil("Estado civil inválido")

    # Implementación del cálculo de la cuota de hipoteca inversa
    cuota = (valor_inmueble * tasa_interes) / (1 + max(edad_propietario, edad_conyuge))

    pass

