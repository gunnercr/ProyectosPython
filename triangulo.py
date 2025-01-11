
"""Variables seleccionadas"""
lado1 =int(input("Ingrese el lado 1. "))
lado2 =int(input("Ingrese el lado 2. "))
lado3 =int(input("Ingrese el lado 3. "))

if lado1 == lado2 == lado3:
    print("Este es un triángulo equilátero. ")
elif lado1 != lado2 and lado1 != lado3 and lado2 !=lado3:
    print("Este triángulo es escaleno. ")
elif lado1 == lado2 or  lado1 == lado3 or lado2 == lado3:
    print("El triángulo es isósceles. ")