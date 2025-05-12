# Decoración: Nombre del Algoritmo
print("-------------------------------------------------------")
print("Complemento 6: INVERTIR NÚMERO.")
print("-------------------------------------------------------")

# Inicializar
aux2 = 0

# Entrada
n = int(input("Ingrese un número: "))
original = n  # Guardar el número original para mostrar al final

# Proceso
while n > 0:
    aux = n % 10          # Obtener el último dígito
    aux2 = aux2 * 10 + aux  # Formar el número invertido
    n = n // 10           # Eliminar el último dígito

# Salida
print("\nSALIDA: ")
print("-------------------------------------------------------")
print(f"El número invertido de {original} es: {aux2}")
