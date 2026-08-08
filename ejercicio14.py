# Crear un programa para calcular la nota final del estudiante en base a 2 exámenes, los exámenes cuentan con un porcentaje distinto de la nota final. nota_1 cuenta como el 40% de la nota final; nota_2 cuenta como el 60% de la nota final. Tener en cuenta: números, print, input, variables, operaciones matemáticas, cadena de texto. Los datos deben guardarse en variables y deben ser dinámicos por medio de input.

# Definición de variables y pedido de datos al usuario (variables, numeros, input)

nota_1 = float(input("\nBienvenido/a, ingrese la nota del primer exámen: ")) 

nota_2 = float(input("\nA continuación, ingrese la nota del segundo exámen: "))

# Cálculo de la nota final (operaciones matemáticas)

nota_final = (nota_1 * 0.4) + (nota_2 * 0.6)

# Muestra por pantalla el resultado (print, cadena de texto)

print(f"\nLa nota final del estudiante es: {nota_final} \n")