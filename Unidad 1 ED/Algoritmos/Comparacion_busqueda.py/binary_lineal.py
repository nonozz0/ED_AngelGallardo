import time
import random

# -----------------------------
# Funciones de Búsqueda
# -----------------------------
def busqueda_lineal(lista, objetivo):
    # Recorremos la lista elemento por elemento
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

def busqueda_binaria(lista, objetivo):
    # Busqueda binaria en lista ordenada
    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1


# -----------------------------
# Experimento
# -----------------------------
tamanos = [1000, 10000, 50000, 100000]

print("Tamaño | Lineal (s) | Binaria (s) | Ratio")
for n in tamanos:
    lista = list(range(n))

    # Seleccionamos 5 elementos existentes y 5 no existentes
    existentes = random.sample(lista, 5)
    no_existentes = [n+i for i in range(5)]
    objetivos = existentes + no_existentes

    # Medir tiempo Lineal
    inicio = time.perf_counter()
    for numero in objetivos:
        busqueda_lineal(lista, numero)
    fin = time.perf_counter()
    tiempo_lineal = (fin - inicio) / len(objetivos)

    # Medir tiempo Binaria
    inicio = time.perf_counter()
    for numero in objetivos:
        busqueda_binaria(lista, numero)
    fin = time.perf_counter()
    tiempo_binaria = (fin - inicio) / len(objetivos)

    # Calcular ratio
    ratio = tiempo_lineal / tiempo_binaria
    print(f"{n} | {tiempo_lineal:.6f} | {tiempo_binaria:.6f} | {ratio:.2f}")
