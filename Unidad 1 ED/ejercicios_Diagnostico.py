#ejercicio 1
print("\nejercicio 1\n")
n = int(input("ingrese el número máximo a contar impares: "))

for x in range(n+1):
    if x % 2 != 0:
        print(x)
        
#ejercicio 2
print("\nejercicio 2\n")
def suma_array():
    array = (1, 2, 3, 4, 5, 6, 7, 8)
    print(sum(array))
    
suma_array()
