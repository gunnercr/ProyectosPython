
producto = float(input("¿Cuál es le precio del producto? "))
descuento = int(input("¿Cuánto es el descuento que quieres aplicar? "))
aplicado = int((descuento/100)*producto)

precio_final= float(producto-aplicado)


if descuento >= 50:

    print("Tienes un descuento especial!!! te queda en: ", precio_final)

else:
    print("Con el descuento el producto queda en: ", precio_final)

