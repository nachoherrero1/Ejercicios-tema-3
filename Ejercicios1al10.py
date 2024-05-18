def main():

    # 1. Fibonacci
    def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)

    n = 10
    resultado_fibonacci = fibonacci(n)
    print(f"1. Fibonacci: {resultado_fibonacci}")

    # 2. Suma de números enteros
    def suma_enteros(n):
        return 0 if n == 0 else n + suma_enteros(n-1)

    n = 5
    resultado_suma_enteros = suma_enteros(n)
    print(f"2. Suma de números enteros hasta {n}: {resultado_suma_enteros}")

    # 3. Producto de dos números enteros
    def producto(a, b):
        return 0 if b == 0 else a + producto(a, b-1)

    a, b = 3, 4
    resultado_producto = producto(a, b)
    print(f"3. Producto de {a} y {b}: {resultado_producto}")

    # 4. Potencia de un número entero
    def potencia(base, exponente):
        return 1 if exponente == 0 else base * potencia(base, exponente-1)

    base, exponente = 2, 3
    resultado_potencia = potencia(base, exponente)
    print(f"4. Potencia de {base}^{exponente}: {resultado_potencia}")

    # 5. Conversión de número romano a decimal
    def valor_romano(letra):
        if letra == 'I':
            return 1
        elif letra == 'V':
            return 5
        elif letra == 'X':
            return 10
        # Agregar el resto de las letras romanas con sus valores
        else:
            return 0

    def romano_a_decimal(romano):
        if len(romano) == 0:
            return 0
        elif len(romano) == 1:
            return valor_romano(romano)
        else:
            if valor_romano(romano[0]) < valor_romano(romano[1]):
                return valor_romano(romano[1]) - valor_romano(romano[0]) + romano_a_decimal(romano[2:])
            else:
                return valor_romano(romano[0]) + romano_a_decimal(romano[1:])

    romano = "XIV"
    resultado_romano_decimal = romano_a_decimal(romano)
    print(f"5. Conversión de {romano} a decimal: {resultado_romano_decimal}")

    # 6. Invertir una secuencia de caracteres
    def invertir_secuencia(secuencia):
        if len(secuencia) == 0:
            return secuencia
        else:
            return invertir_secuencia(secuencia[1:]) + secuencia[0]

    secuencia = "hello"
    resultado_invertir_secuencia = invertir_secuencia(secuencia)
    print(f"6. Invertir la secuencia '{secuencia}': {resultado_invertir_secuencia}")

    # 7. Calcular serie
    def calcular_serie(n):
        return 0 if n == 0 else n + calcular_serie(n-1)

    n = 5
    resultado_serie = calcular_serie(n)
    print(f"7. Calcular serie hasta {n}: {resultado_serie}")

    # 8. Decimal a binario
    def decimal_a_binario(decimal):
        if decimal == 0:
            return '0'
        elif decimal == 1:
            return '1'
        else:
            return decimal_a_binario(decimal // 2) + str(decimal % 2)

    decimal = 13
    resultado_decimal_a_binario = decimal_a_binario(decimal)
    print(f"8. Decimal {decimal} en binario: {resultado_decimal_a_binario}")

    # 9. Logaritmo entero en una base dada
    def logaritmo_entero(n, b):
        if n < b:
            return 0
        else:
            return 1 + logaritmo_entero(n // b, b)

    n, b = 16, 2
    resultado_logaritmo_entero = logaritmo_entero(n, b)
    print(f"9. Logaritmo entero de {n} en base {b}: {resultado_logaritmo_entero}")

    # 10. Cantidad de dígitos de un número entero
    def contar_digitos(numero):
        if numero < 10:
            return 1
        else:
            return 1 + contar_digitos(numero // 10)

    numero = 123456
    resultado_contar_digitos = contar_digitos(numero)
    print(f"10. Cantidad de dígitos de {numero}: {resultado_contar_digitos}")

if __name__ == "__main__":
    main()