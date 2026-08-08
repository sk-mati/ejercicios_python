# Determinar mentalmente los resultados anotarlos en un papel y luego comprobar ejecutando el programa.
#     • Igualdad
# print(4==4)
# print(4==5)
# print(4==4.0)
# print(0==False)   
# print("asd"=="asd")
# print("asd"=="asdf") 
# print(2=="2")
# print([1, 2, 3] == [1, 2, 5])

#     • Desigualdad
# print(4!=4)  
# print(4!=5)     
# print(4!=4.0)        
# print(0!=False)      
# print("asd"!="asd") 
# print("asd"!="asdf") 
# print(2!="2")        
# print([1, 2, 3] != [1, 2, 3])



#     • Mayor que
# print(23 > 1)
# print(2 > 14)
# print("2" > "1")
# print("2" > 1)
# print("Arnold" > "Silvester")
# print(33 > 33)
# print(3.14 > 3.15)
# print(7.45 > 7)

#     • Menor que
# print(35 < 34)
# print(77 < 77)
# print(7 < 45)
# print(7.26 < 45)
# print(7.26 < "7.28")
# print("7.26" < "7.28")
# print("True" < "False")
# print("Falso" < "Verdadero")

#     • Mayor o igual que
# print(3 >= 3) 
# print(5 >= 3.4) 
# print(False > True) 
# print([3,4] >= [3,5])
# print("Hola " >= "Hola")
# print([3,4] >= 77)
# print("Python" >= "Python")
# print(3.004 >= 3.0) 

#     • Menor o igual que
# print(3 <= 2.9)
# print(3 <= 2.99999999999999999)
# print(45 <= 45)
# print([3, 4, 89] <= [3, 5, 87])
# print(False <= 0)
# print("Vamos" <= "vamos")
# print(345.23 <= 4)
# print(345.23 <= "4")

# Papel

# igualdad
print("\nIgualdad\n")
print(4==4) # True
print(4==5) # False
print(4==4.0) # True
print(0==False) # True
print("asd"=="asd") # True
print("asd"=="asdf") # False 
print(2=="2") # False
print([1, 2, 3] == [1, 2, 5]) # False

# desigualdad
print("\nDesigualdad\n")
print(4!=4) # False  
print(4!=5) # True     
print(4!=4.0) # False        
print(0!=False) # False      
print("asd"!="asd") # False
print("asd"!="asdf") # True
print(2!="2") # True    
print([1, 2, 3] != [1, 2, 3]) # False

# mayor que
print("\nMayor que\n")
print(23 > 1) # True
print(2 > 14) # False
print("2" > "1") # True por su valor unicode / ASCII
#print("2" > 1) # No se puede realizar
print("Arnold" > "Silvester") # False
print(33 > 33) # False
print(3.14 > 3.15) # False
print(7.45 > 7) # True

# menor que
print("\nMenor que\n")
print(35 < 34) # False 
print(77 < 77) # False
print(7 < 45) # True
print(7.26 < 45) # True
#print(7.26 < "7.28") # No se puede realizar
print("7.26" < "7.28") # True
print("True" < "False") # False
print("Falso" < "Verdadero") # True

# mayor o igual que
print("\nMayor o igual que\n")
print(3 >= 3) # True
print(5 >= 3.4) # True
print(False > True) # False porque False = 0 y True = 1
print([3,4] >= [3,5]) # False
print("Hola " >= "Hola") # True
#print([3,4] >= 77) # No se puede realizar
print("Python" >= "Python") # True
print(3.004 >= 3.0) # True

# menor o igual que
print("\nMenor o igual que\n")
print(3 <= 2.9) # False
print(3 <= 2.99999999999999999) # True porque redondea
print(45 <= 45) # True
print([3, 4, 89] <= [3, 5, 87]) # True porque compara en orden de izquierda a derecha
print(False <= 0) # True
print("Vamos" <= "vamos") # True por su valor unicode
print(345.23 <= 4) # False
#print(345.23 <= "4") # No se puede realizar