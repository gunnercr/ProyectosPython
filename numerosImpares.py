

lista=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,20]
cont_impar=0



for x in lista:
    if x % 2 != 0:
        cont_impar +=1

print("La cantidad de impares es: ", cont_impar)