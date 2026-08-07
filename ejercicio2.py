# Pide al usuario que ingrese un número decimal (float). Convierte ese número a un entero y luego a una cadena de texto. Muestra ambos resultados.

numero_decimal = float(input("\nBienvenido/a, ingrese un número decimal: ")) # Pedido

numero_entero = int(numero_decimal) # Conversión de decimal a entero

cadena_de_texto = str(numero_entero) # Conversión de entero a cadena de texto

# Muestra por pantalla los resultados

print("\n- La variable 'numero_entero' contiene el valor -> ", numero_entero)
print("\nY su clase es: ", type(numero_entero))

print("\n- La variable 'cadena_de_texto' contiene el mismo valor -> ", cadena_de_texto)
print("\nPero su clase difiere de la anterior variable, ya que se realizó una conversión y es: ", type(cadena_de_texto), "\n")