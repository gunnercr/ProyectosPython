
lista = [12, -5, 7, 22, -8, 0, 19, -3, 45, -12, 33, 8, -20,44,70]
contador_pares = 0
contador_impares = 0
num_mayor = (lista[0])
num_menor = (lista[0])

if not lista:
    print("La lista está vacía.")
else:
    for x in lista:
        if x % 2 == 0:
            contador_pares += 1
        else:
            contador_impares += 1
        if x > num_mayor:
            num_mayor = x

        if x < num_menor:
            num_menor = x



print("En la lista hay ", contador_pares, " números pares.")
print("En la lista hay ", contador_impares, " números impares.")
print("En la lista el número mayor es  ", num_mayor)
print("En la lista el número menor es  ", num_menor)