n = int(input("ingrese un número entero positivo: "))
if n > 1:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print("No es primo")
            break
    else:
        print("Es primo")
else:
    print("No es primo")
    