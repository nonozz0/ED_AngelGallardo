from random import randint

num_aleatorio = randint(1, 10)

num_elegido = int(input("ingresa un número del 1 al 10: "))
while True:
    if num_aleatorio == num_elegido:
        print("Felicidades! adivinaste")
        break
    else:
        num_elegido = int(input("Lo siento, intenta nuevamente: "))
    