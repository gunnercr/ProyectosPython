from itertools import repeat

import random

numero_secreto = random.randint(1,100)

print("Bienvenido o bienvenida al juego de adivinanza!")
print("¿Crees que puedes adivinar el número que estoy pensando?")

while True:
    intento = int(input("Ingrese su número: "))
    if intento > numero_secreto:
        print("Demasiado alto, intenta un número más bajo")
    elif intento < numero_secreto:
        print("Demasiado bajo, intenta un número más alto")
    else:
        print("Felicidades, adivinaste el número! ")
        break






