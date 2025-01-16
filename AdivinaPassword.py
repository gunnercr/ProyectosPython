
contra= ("python123")
print("Este es un sistema de seguridad.")

while True:
    intento = input("Ingrese la contraseña: ")

    if intento != contra:
        print("Contraseña incorrecta, ingresela nuevamente.")
    else:
        print("Contraseña correcta, puede utilizar el sistema.")
        break