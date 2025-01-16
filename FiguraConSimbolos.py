fila= (int(input("¿Cuántas filas? ")))
columna= (int(input("¿Cuántas columnas? ")))
simbolo= (input("Inserte un simbolo: "))

for i in range (fila):
    for j in range (columna):
        print(simbolo , end="")
    print()

