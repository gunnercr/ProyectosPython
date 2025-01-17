lista= [9,5,4,10,3,1,18,25,0,46,11]
mayor=(lista[0])


for x in lista:
    if x > mayor:
        mayor=x

print("El número mayor de la lista es: ", mayor)