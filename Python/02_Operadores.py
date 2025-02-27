# Operadores Aritméticos
print(3 + 4) # Suma
print(3 - 4) # Resta
print(3 * 4) # Multiplicación
print(3 / 4) # División
print(10 % 3) # Para comprobar si al multiplicar con el No. de la dcha no sobra nada en el No. de la izda
print(10 // 3) # División con resultado int
print(2 ** 3) #Exponente
print(2 ** 3 + 3 - 7 / 1 // 4) # Ejercicio con operadores

print("Hola " + "Python" + " ¿Qué tal?")
print("Hola " + str(5))
print("Hola " * 5)
print("Hola " * (2 ** 3))

my_float = 2.5 * 2
print("Hola " * int(my_float))

# Operadores Comparativos
print(3 > 4) # Mayor que
print(3 < 4) # Menor que
print(3 >= 4) # Mayor o igual que
print(3 <= 4) # Menor o igual que
print(3 == 4) # Igual que
print(3 != 4) # Distinto que
print(3 > 4 == 2)

print("Hola" > "Python")
print("Hola" < "Python")
print("aaaa" >= "AAAA") # Ordenación Alfabética por ASCII
print(len("aaaa") >= len("abaa")) # Cuenta caracteres
print("Hola" <= "Python")
print("Hola" == "Hola")
print("Hola" != "Python")

# Operadores Lógicos
print(3 > 4 and "Hola" > "Python") 
print(3 > 4 or "Hola" > "Python")
print(3 < 4 and "Hola" < "Python") 
print(3 < 4 or "Hola" > "Python")
print(3 < 4 or ("Hola" > "Python" and 4 == 4))
print(not(3 > 4))