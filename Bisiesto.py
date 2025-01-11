año = int(input("¿Qué año estamos? "))

if (año % 4 == 0 and año % 100 != 0) or (año %400 == 0):
    print("Este es un año bisiesto")
else:
    print("Este es un año normal de 365 días.")
