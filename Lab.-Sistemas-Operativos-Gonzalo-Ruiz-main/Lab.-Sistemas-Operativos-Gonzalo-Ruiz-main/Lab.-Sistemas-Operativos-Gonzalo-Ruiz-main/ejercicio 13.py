# Decoración: Nombre del Algoritmo
print("-------------------------------------------------------")
print("Complemento 7: DETERMINAR SI UN NÚMERO ES PRIMO.")
print("-------------------------------------------------------")

# Entradas
n = int(input("Ingrese un número: "))

# Validación de número
if n <= 1:
    print("\nSALIDA: ")
    print("-------------------------------------------------------")
    print(n, "no es un número primo (los primos son mayores que 1).")
else:
    # Proceso: Verificar si es primo
    es_primo = True
    for i in range(2, int(n ** 0.5) + 1):  # Optimización: solo hasta la raíz cuadrada
        if n % i == 0:
            es_primo = False
            break  # Si encuentra un divisor, rompe el ciclo

    # Salida
    print("\nSALIDA: ")
    print("-------------------------------------------------------")
    if es_primo:
        print(n, "es un número primo.")
    else:
        print(n, "no es un número primo.")
