def main():
 # 11. Invertir un número entero sin convertirlo a cadena
    def invertir_entero(numero):
        def invertir_aux(numero, resultado):
            if numero == 0:
                return resultado
            else:
                return invertir_aux(numero // 10, resultado * 10 + numero % 10)
        return invertir_aux(numero, 0)

    numero = 123456
    resultado_invertir_entero = invertir_entero(numero)
    print(f"11. Invertir el número entero {numero}: {resultado_invertir_entero}")

    # 12. Algoritmo de Euclides para el Máximo Común Divisor (MCD)
    def mcd(a, b):
        if b == 0:
            return a
        else:
            return mcd(b, a % b)

    a, b = 48, 18
    resultado_mcd = mcd(a, b)
    print(f"12. MCD de {a} y {b}: {resultado_mcd}")

    # 13. Algoritmo de Euclides para el Mínimo Común Múltiplo (MCM)
    def mcm(a, b):
        return a * b // mcd(a, b)

    resultado_mcm = mcm(a, b)
    print(f"13. MCM de {a} y {b}: {resultado_mcm}")

    # 14. Suma de los dígitos de un número entero
    def suma_digitos(numero):
        if numero < 10:
            return numero
        else:
            return numero % 10 + suma_digitos(numero // 10)

    numero = 12345
    resultado_suma_digitos = suma_digitos(numero)
    print(f"14. Suma de dígitos de {numero}: {resultado_suma_digitos}")

    # 15. Raíz cuadrada entera de un número entero
    def raiz_cuadrada_entera(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            x = n // 2
            prev = 0
            while x != prev:
                prev = x
                x = (x + n // x) // 2
            return x

    n = 16
    resultado_raiz_cuadrada_entera = raiz_cuadrada_entera(n)
    print(f"15. Raíz cuadrada entera de {n}: {resultado_raiz_cuadrada_entera}")

    # 16. Sucesión geométrica con a1=2 y razón r=-3
    def sucesion_geometrica(n):
        if n == 1:
            return 2
        else:
            return -3 * sucesion_geometrica(n-1)

    def valores_sucesion(n):
        return [sucesion_geometrica(i) for i in range(1, n+1)]

    n = 5
    resultado_sucesion_geometrica = valores_sucesion(n)
    print(f"16. Valores de la sucesión geométrica hasta {n}: {resultado_sucesion_geometrica}")

    # 17. Mostrar vector de atrás hacia adelante
    def mostrar_vector_atras(vec, i):
        if i < 0:
            return
        else:
            print(vec[i])
            mostrar_vector_atras(vec, i-1)

    vec = [1, 2, 3, 4, 5]
    mostrar_vector_atras(vec, len(vec)-1)

    # 18. Recorrer una matriz y mostrar sus valores
    def mostrar_matriz(mat, i, j):
        if i == len(mat):
            return
        elif j == len(mat[i]):
            mostrar_matriz(mat, i+1, 0)
        else:
            print(mat[i][j])
            mostrar_matriz(mat, i, j+1)

    matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    mostrar_matriz(matriz, 0, 0)

    # 19. Cálculo de sucesión recursiva dada
    def sucesion_recursiva(n):
        if n == 0:
            return 1
        elif n == 1:
            return 2
        else:
            return 2 * sucesion_recursiva(n-1) - 3 * sucesion_recursiva(n-2)

    n = 5
    resultado_sucesion_recursiva = sucesion_recursiva(n)
    print(f"19. Valor de la sucesión recursiva en {n}: {resultado_sucesion_recursiva}")

    # 20. Búsqueda secuencial recursiva con centinela
    def busqueda_secuencial(lista, valor, indice=0):
        if indice == len(lista):
            return False
        elif lista[indice] == valor:
            return True
        else:
            return busqueda_secuencial(lista, valor, indice + 1)

    lista = [1, 2, 3, 4, 5]
    valor = 3
    resultado_busqueda_secuencial = busqueda_secuencial(lista, valor)
    print(f"20. Búsqueda secuencial de {valor} en lista: {resultado_busqueda_secuencial}")

if __name__ == "__main__":
    main()