import time
import random

# -----------------------------
# Bubble Sort
# -----------------------------
def bubble_sort(lista):
    lista_ordenada = lista.copy()
    n = len(lista_ordenada)

    for i in range(n):
        for j in range(0, n-i-1):
            if lista_ordenada[j] > lista_ordenada[j+1]:
                temp = lista_ordenada[j]
                lista_ordenada[j] = lista_ordenada[j+1]
                lista_ordenada[j+1] = temp
    return lista_ordenada


# -----------------------------
# 2.1 Evaluación por tamaño
# -----------------------------
dimensiones = [100, 500, 1000, 5000, 10000]

print("Dim | Bubble (s) | Sorted (s) | Relación")
for n in dimensiones:
    numeros = random.sample(range(n*10), n)

    # Bubble Sort
    inicio = time.perf_counter()
    bubble_sort(numeros)
    fin = time.perf_counter()
    tiempo_bubble = fin - inicio

    # Python sorted
    inicio = time.perf_counter()
    sorted(numeros)
    fin = time.perf_counter()
    tiempo_sorted = fin - inicio

    relacion = tiempo_bubble / tiempo_sorted
    print(f"{n} | {tiempo_bubble:.6f} | {tiempo_sorted:.6f} | {relacion:.2f}")


# -----------------------------
# 2.2 Casos específicos
# -----------------------------
secuencia_ordenada = list(range(1000))
secuencia_inversa = list(range(1000, 0, -1))
secuencia_casi = [x if x % 100 != 0 else x+500 for x in range(1000)]

escenarios = {
    "Ordenado": secuencia_ordenada,
    "Inverso": secuencia_inversa,
    "Casi ordenado": secuencia_casi
}

print("\nEscenario | Bubble (s) | Sorted (s)")
for nombre in escenarios:
    numeros = escenarios[nombre]

    inicio = time.perf_counter()
    bubble_sort(numeros)
    fin = time.perf_counter()
    tiempo_bubble = fin - inicio

    inicio = time.perf_counter()
    sorted(numeros)
    fin = time.perf_counter()
    tiempo_sorted = fin - inicio

    print(f"{nombre} | {tiempo_bubble:.6f} | {tiempo_sorted:.6f}")
