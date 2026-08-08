# Determinar mentalmente los resultados, anotarlos en un papel y luego comprobar ejecutando el programa.

#     • and
# expresion1 = 3 > 2 and 4 > 2
# expresion2 = 45 < 32 and 45 == 45
# expresion3 = 4 < 32 and 45 == 45 and 33 != 78
# expresion4 = 3 == 3.0 and "b" > "a" and 999 >= 990

#     • or
# expresion1 = 9 < 2 or 4 > 2
# expresion2 = 80 < 79 or 14 > 14.5 or 7 > 57
# expresion3 = "aaa" == "aaa" or 1 > 0.5
# expresion3 = "aaa" == "aaa" or 1 > 0.5
# expresion4 = "A" != "a" or "Francia" == "Argentina" or 3 < "a"

#     • not
# expresion1 = not 9 == 2
# expresion2 = not 45 != 45
# expresion3 = not 875 > 678
# expresion4 = not "Julieta" > "Juliana"
# expresion5 = not 1
# expresion6 = not 0.0
# expresion7 = not " "
# expresion8 = not "False"
# expresion9 = not True

#     • De todo un poco
# expresion1 = 8 * 4 and 6 > 3 and 34 >= 33
# expresion2 = not 4 > 5 or 5 ** 2 and 6 != 3
# expresion3 = 43 + (22 > 4)
# expresion4 = not 43 or 99 >= 999
# expresion5 = (not 43 or 99 >= 999) and 2 ** 2 or (4 != 43 and "Python" > "Python Recargado")
# expresion6 = 6 and 6 + 34
# expresion7 = 0.0 and 6 + 34
# expresion8 = not 0.0 and 5 + 5
# expresion9 = "23" == "23" and 34 >= 34 or (241 < 98 or 436 <= 1988) and not 987 > 76

# Tabla de verdad lógica

# |  p  |  q  |  p and q  |  p or q  |  not p  |  not q  |
# |  V  |  V  |     V     |     V    |    F    |    F    |
# |  V  |  F  |     F     |     V    |    F    |    V    |
# |  F  |  V  |     F     |     V    |    V    |    F    |
# |  F  |  F  |     F     |     F    |    V    |    V    |

# Papel

# and
expresion1 = 3 > 2 and 4 > 2
expresion2 = 45 < 32 and 45 == 45
expresion3 = 4 < 32 and 45 == 45 and 33 != 78
expresion4 = 3 == 3.0 and "b" > "a" and 999 >= 990

print(f"\nand\n")
print(f"La variable expresion1 está compuesta por valores: True - and - True. Su valor booleano final es True. Verifico: {expresion1}")
print(f"La variable expresion2 está compuesta por valores: False - and - True. Su valor booleano final es False. Verifico: {expresion2}")
print(f"La variable expresion3 está compuesta por valores: True - and - True - and - True. Su valor booleano final es True. Verifico: {expresion3}")
print(f"La variable expresion4 está compuesta por valores: True - and - True - and - True. Su valor booleano final es True. Verifico: {expresion4}")

# or
expresion5 = 9 < 2 or 4 > 2
expresion6 = 80 < 79 or 14 > 14.5 or 7 > 57
expresion7 = "aaa" == "aaa" or 1 > 0.5
expresion8 = "A" != "a" or "Francia" == "Argentina" or 3 < "a"

print(f"\nor\n")
print(f"La variable expresion1 está compuesta por valores: False - or - True. Su valor booleano final es True. Verifico: {expresion5}")
print(f"La variable expresion2 está compuesta por valores: False - or - False - or - False. Su valor booleano final es False. Verifico: {expresion6}")
print(f"La variable expresion3 está compuesta por valores: True - or - True. Su valor booleano final es True. Verifico: {expresion7}")
print(f"La variable expresion4 está compuesta por valores: True - or - False - or - False. Su valor booleano final es True. Verifico: {expresion8}")

# not
expresion9 = not 9 == 2
expresion10 = not 45 != 45
expresion11 = not 875 > 678
expresion12 = not "Julieta" > "Juliana"
expresion13 = not 1 # True equivale a 1
expresion14 = not 0.0 # False equivale a 0
expresion15 = not " " # Toda cadena de texto es True
expresion16 = not "False" 
expresion17 = not True

print(f"\nnot\n")
print(f"La variable expresion9 tiene un valor not False. Su valor final es True. Verifico: {expresion9}")
print(f"La variable expresion10 tiene un valor not False. Su valor final es True. Verifico: {expresion10}")
print(f"La variable expresion11 tiene un valor not True. Su valor final es False. Verifico: {expresion11}")
print(f"La variable expresion12 tiene un valor not True. Su valor final es False. Verifico: {expresion12}")
print(f"La variable expresion13 tiene un valor not True. Su valor final es False. Verifico: {expresion13}")
print(f"La variable expresion14 tiene un valor not False. Su valor final es True. Verifico: {expresion14}")
print(f"La variable expresion15 tiene un valor not True. Su valor final es False. Verifico: {expresion15}")
print(f"La variable expresion16 tiene un valor not True. Su valor final es False. Verifico: {expresion16}")
print(f"La variable expresion17 tiene un valor not True. Su valor final es False. Verifico: {expresion17}")

# De todo un poco
expresion18 = 8 * 4 and 6 > 3 and 34 >= 33
expresion19 = not 4 > 5 or 5 ** 2 and 6 != 3
expresion20 = 43 + (22 > 4)
expresion21 = not 43 or 99 >= 999
expresion22 = (not 43 or 99 >= 999) and 2 ** 2 or (4 != 43 and "Python" > "Python Recargado")
expresion23 = 6 and 6 + 34
expresion24 = 0.0 and 6 + 34
expresion25 = not 0.0 and 5 + 5
expresion26 = "23" == "23" and 34 >= 34 or (241 < 98 or 436 <= 1988) and not 987 > 76 # Jerarquía

print(f"\nDe todo un poco\n")
print(f"La variable expresion18 está compuesta por valores: True - and - True - and - True. Su valor booleano final es True. Verifico: {expresion18}")
print(f"La variable expresion19 está compuesta por valores: True - or - True - and - True. Su valor booleano final es True. Verifico: {expresion19}")
print(f"La variable expresion20 está compuesta por valores: 43 - + - 1. Su valor final es 44. Verifico: {expresion20}")
print(f"La variable expresion21 está compuesta por valores: False - or - False. Su valor booleano final es False. Verifico: {expresion21}")
print(f"La variable expresion22 está compuesta por valores: False - or - False - and - True - or - True - and - False. Su valor booleano final es False. Verifico: {expresion22}")
print(f"La variable expresion23 está compuesta por valores: 6 (True) - and - 6 - + - 34. Su valor final es 40. Verifico: {expresion23}")
print(f"La variable expresion24 está compuesta por valores: 0.0 (False) - and - 6 - + - 34. Su valor final es 0.0. Verifico: {expresion24}")
print(f"La variable expresion25 está compuesta por valores: not 0.0 (True) - and - 5 - + - 5. Su valor final es 10. Verifico: {expresion25}")
print(f"La variable expresion26 está compuesta por valores: True - and - True - or - (False - or - True) - and - False. Su valor final es True. Verifico: {expresion26}")