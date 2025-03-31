def suma_varios_numeros(*numeros):
    if len(numeros) > 4:
        return sum(numeros)
    else:
        return "Debes ingresar más de cuatro números."

# Ejemplo de uso
print(suma_varios_numeros(1, 2, 3, 4, 5))  # Salida: 15