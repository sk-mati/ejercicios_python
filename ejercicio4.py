# Pide al usuario que ingrese el valor de la base y la altura de un triángulo (float). Calcula el área del triángulo utilizando la fórmula área = (base * altura) / 2 y muestra el resultado.

base = float(input("\nBienvenido, ingrese el valor de la base del triángulo (en metros): ")) # Pedido de la base del triángulo

altura = float(input("\nA continuación, ingrese el valor de la altura del triángulo (en metros): ")) # Pedido de la altura del triángulo

area = (base * altura) / 2 # Cálculo del área del triángulo

print(f"\nEl área del triángulo es igual a {area} metros cuadrados.\n") # Muestra por pantalla
