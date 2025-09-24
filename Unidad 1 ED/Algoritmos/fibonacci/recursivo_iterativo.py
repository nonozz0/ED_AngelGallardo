import time

# -----------------------------
# Fibonacci Recursivo
# -----------------------------
def fib_recursivo(n):
    if n <= 1:
        return n
    return fib_recursivo(n-1) + fib_recursivo(n-2)

# Fibonacci Iterativo
def fib_iterativo(n):
    a = 0
    b = 1
    for i in range(n):
        temp = a + b
        a = b
        b = temp
    return a

# -----------------------------
# Tiempos de cálculo
# -----------------------------
valores_n = [5, 10, 20, 30, 35]

print("n | Fibonacci | Recursivo (s) | Iterativo (s)")
for n in valores_n:
    # Recursivo
    inicio = time.perf_counter()
    res_rec = fib_recursivo(n)
    fin = time.perf_counter()
    tiempo_rec = fin - inicio

    # Iterativo
    inicio = time.perf_counter()
    res_it = fib_iterativo(n)
    fin = time.perf_counter()
    tiempo_it = fin - inicio

    print(f"{n} | {res_it} | {tiempo_rec:.6f} | {tiempo_it:.6f}")


# -----------------------------
# Límites prácticos
# -----------------------------
print("\nLímites Recursivo (hasta n=40):")
for n in range(36, 41):
    inicio = time.perf_counter()
    try:
        fib_recursivo(n)
        fin = time.perf_counter()
        print(f"n={n} en {fin - inicio:.2f} s")
    except RecursionError:
        print(f"n={n} demasiado grande")

print("\nLímites Iterativo:")
for n in [10000, 50000, 100000]:
    inicio = time.perf_counter()
    fib_iterativo(n)
    fin = time.perf_counter()
    print(f"n={n} en {fin - inicio:.4f} s")
