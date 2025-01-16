import math



print("Esta es una calculadora de promedios")
print("Ingrese 1 a 1 sus calificaciones")
print("Cuando haya terminado, coloque -1 para realizar el cáculo.")

suma=0
contador=0

while True:
    materia = int(input("Inserte su calificación: "))

    if materia == -1:
        break
    elif materia >=0:
        suma += materia
        contador += 1
        print("Calificación registrada.")
    else:
        print("Calificación inválida, ingrese un valor válido.")

if contador >0:
    promedio = suma / contador
    print("El promedio de tus calificaciones es: ", promedio)
else:
    print("No ingresaste una calificación válida")


