# Escribe un programa que convierta una cantidad en metros a otras unidades (centímetros, milímetros, pulgadas). Pide al usuario que ingrese la cantidad en metros y realiza las conversiones utilizando operadores aritméticos. Muestra todas las conversiones.

metros = float(input("\nBienvenido/a, ingrese la cantidad numérica (en metros): ")) # Pedido al usuario

centimetros = metros * 100 # Conversión de metros a centímetros

milimetros = metros * 1000 # Conversión de metros a milímetros

pulgadas = metros / 0.0254 # Conversión de metros a pulgadas

# Muestra por pantalla

print(f"\nLa cantidad ingresada es de {metros} metros.")
print(f"\nLa cantidad de {metros} metros convertida a centímetros es de {centimetros} centímetros.")
print(f"\nLa cantidad de {metros} metros convertida a milímetros es de {milimetros} milímetros.")
print(f"\nLa cantidad de {metros} metros convertida a pulgadas es de {pulgadas} pulgadas.\n")