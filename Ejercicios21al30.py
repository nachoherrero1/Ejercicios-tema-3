def main():
 
    # 21. Búsqueda binaria recursiva en lista ordenada
    def busqueda_binaria_recursiva(lista, valor, inicio=0, fin=None):
        if fin is None:
            fin = len(lista) - 1
        if inicio > fin:
            return False
        medio = (inicio + fin) // 2
        if lista[medio] == valor:
            return True
        elif lista[medio] < valor:
            return busqueda_binaria_recursiva(lista, valor, medio + 1, fin)
        else:
            return busqueda_binaria_recursiva(lista, valor, inicio, medio - 1)

    lista_ordenada = [1, 2, 3, 4, 5]
    valor = 3
    resultado_busqueda_binaria_recursiva = busqueda_binaria_recursiva(lista_ordenada, valor)
    print(f"21. Búsqueda binaria de {valor} en lista ordenada: {resultado_busqueda_binaria_recursiva}")

    # 22. Uso de la fuerza en la mochila Jedi
    def usar_la_fuerza(mochila, indice=0):
        if indice == len(mochila):
            return False, 0
        elif mochila[indice] == "sable de luz":
            return True, indice + 1
        else:
            encontrado, pasos = usar_la_fuerza(mochila, indice + 1)
            return encontrado, pasos + 1

    mochila = ["libro", "comida", "sable de luz", "mapa"]
    encontrado, pasos = usar_la_fuerza(mochila)
    print(f"22. ¿Se encontró un sable de luz en la mochila? {encontrado}. Pasos necesarios: {pasos}")

    # 23. Salida del laberinto
    def salir_del_laberinto(laberinto, x=0, y=0, solucion=None):
        if solucion is None:
            solucion = []
        n = len(laberinto)
        if x == n - 1 and y == n - 1:
            solucion.append((x, y))
            return True, solucion
        elif 0 <= x < n and 0 <= y < n and laberinto[x][y] == 0 and (x, y) not in solucion:
            solucion.append((x, y))
            if (salir_del_laberinto(laberinto, x+1, y, solucion)[0] or
                salir_del_laberinto(laberinto, x, y+1, solucion)[0] or
                salir_del_laberinto(laberinto, x-1, y, solucion)[0] or
                salir_del_laberinto(laberinto, x, y-1, solucion)[0]):
                return True, solucion
            solucion.pop()
        return False, solucion

    laberinto = [[0, 1, 0, 0, 0],
                 [0, 1, 0, 1, 0],
                 [0, 0, 0, 1, 0],
                 [0, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0]]
    resultado_salida_laberinto, solucion = salir_del_laberinto(laberinto)
    if resultado_salida_laberinto:
        print("23. Se encontró un camino para salir del laberinto:")
        for fila, columna in solucion:
            print(f"({fila}, {columna}) -> ", end="")
        print("Salida")
    else:
        print("23. No se encontró un camino para salir del laberinto")

    # 24. Torre de Hanói
    def torre_de_hanoi(n, origen, destino, auxiliar):
        if n == 1:
            print(f"Mover disco de {origen} a {destino}")
        else:
            torre_de_hanoi(n-1, origen, auxiliar, destino)
            print(f"Mover disco de {origen} a {destino}")
            torre_de_hanoi(n-1, auxiliar, destino, origen)

    n_discos = 3
    print(f"24. Solución de la Torre de Hanói con {n_discos} discos:")
    torre_de_hanoi(n_discos, 'A', 'C', 'B')

    # 25. Triángulo de Pascal
    def triangulo_de_pascal(n):
        if n == 0:
            return [[1]]
        else:
            triangulo = triangulo_de_pascal(n-1)
            nueva_fila = [1]
            for i in range(1, n):
                nueva_fila.append(triangulo[n-1][i-1] + triangulo[n-1][i])
            nueva_fila.append(1)
            triangulo.append(nueva_fila)
            return triangulo

    filas = 5
    triangulo = triangulo_de_pascal(filas)
    print(f"25. Triángulo de Pascal con {filas} filas:")
    for fila in triangulo:
        print(fila)

    # 26. Colocación de las 8 reinas
    def es_valido(tablero, fila, columna):
        return not any(
            tablero[i] == columna or
            tablero[i] - i == columna - fila or
            tablero[i] + i == columna + fila
            for i in range(fila)
        )

    def colocar_reinas(tablero, fila=0):
        n = len(tablero)  # Asegurar que esta línea esté correctamente indentada
        if fila == n:
            return [tablero[:]]  # Crear una copia del tablero actual
        soluciones = []
        for columna in range(n):
            if es_valido(tablero, fila, columna):
                tablero[fila] = columna
                soluciones.extend(colocar_reinas(tablero, fila+1))
                tablero[fila] = -1  # Restaurar el valor original del tablero
        return soluciones

    tablero = [-1] * 8  # Inicializar el tablero con valores -1
    soluciones = colocar_reinas(tablero)
    print(f"26. Cantidad de soluciones encontradas para las 8 reinas: {len(soluciones)}")


    # 27. Valores de una sucesión geométrica hacia atrás
    def sucesion_geometrica_atras(valor_final, a1, r):
        valores= [valor_final]
        while valor_final != a1:
            valor_final //= r  # División entera para asegurar que el resultado sea un entero
            valores.append(valor_final)
            return valores
    valor_final=1376256
    a1=5.25
    r=4
    valores=sucesion_geometrica_atras(valor_final, a1, r)
    print(f"27. Valores de la sucesión geométrica hacia atrás: {valores}")


    # 28. Cálculo de la bisección de una función
    def biseccion(f, a, b, tol=1e-6):
        if abs(b - a) < tol:
            return (a + b) / 2
        else:
            c = (a + b) / 2
            if f(a) * f(c) < 0:
                return biseccion(f, a, c)
            else:
                return biseccion(f, c, b)

    resultado_biseccion = biseccion(lambda x: x**2 - 2, 0, 2)
    print(f"28. Raíz cuadrada de 2 calculada con bisección: {resultado_biseccion}")

    # 29. Cálculo del método de la secante de una función
    def secante(f, x0, x1, tol=1e-6):
        while abs(x1 - x0) >= tol:
            x0, x1 = x1, x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        return x1

    resultado_secante = secante(lambda x: x**2 - 2, 1, 2)
    print(f"29. Raíz cuadrada de 2 calculada con secante: {resultado_secante}")

    # 30. Cálculo del método de Newton-Raphson de una función
    def newton_raphson(f, df, x0, tol=1e-6):
        while abs(f(x0)) >= tol:
            x0 -= f(x0) / df(x0)
        return x0

    resultado_newton_raphson = newton_raphson(lambda x: x**2 - 2, lambda x: 2*x, 2)
    print(f"30. Raíz cuadrada de 2 calculada con Newton-Raphson: {resultado_newton_raphson}")
if __name__ == "__main__":
    main()