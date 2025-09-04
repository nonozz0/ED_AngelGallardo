# Calculadora de grados Celsius a Fahrenheit
celsius = float(input("Grados Celsius a convertir: "))
fahrenheit = (celsius * 9/5) + 32
resultado = round(fahrenheit, 1)
print(f"Los grados convertidos a Fahrenheit son: {resultado}°F")
