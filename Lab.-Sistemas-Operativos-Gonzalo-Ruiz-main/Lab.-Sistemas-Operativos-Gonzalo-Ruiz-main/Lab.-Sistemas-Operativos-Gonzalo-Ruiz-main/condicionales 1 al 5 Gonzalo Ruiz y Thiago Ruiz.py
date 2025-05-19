# Pedir al usuario que ingrese un número del 1 al 7
dia = int(input("Ingrese un número del 1 al 7 representando un día de la semana (1: lunes, 7: domingo): "))

# Validación de rango
if dia < 1 or dia > 7:
    print("Número no válido. Por favor, ingrese un número entre 1 y 7.")
else:
    # Lógica para determinar si es un día laboral o fin de semana
    if dia >= 1 and dia <= 5:
        print("Es un día laboral.")
    else:
        print("Es fin de semana.")
