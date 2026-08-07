# Dado un número n, verifica si es múltiplo de 3 y, al mismo tiempo, si es mayor que 50. Muestra el resultado de ambas comparaciones en una sola expresión.

n = 77 # Definición de variables 

verificacion = (n % 3 == 0) # Verificación del número (múltiplo)

verificacion_2 = (n > 50) # Verificación del número (mayor)

print(verificacion == verificacion_2) # Muestra la verificación final por pantalla