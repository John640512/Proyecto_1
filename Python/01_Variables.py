# Variables
string_variable = "Mi variable de String"
print(string_variable)

int_variable = 5
print(int_variable)

int_string_variable = str(int_variable)
print(int_string_variable)
print(type(int_string_variable))

float_variable = 8.6
print(float_variable)

complex_variable = 6 + 8j
print(complex_variable)

bool_variable = True
print(bool_variable)

# Concatenación de variables en un print
print(string_variable, int_variable, bool_variable)
print("Esto es lo que dice la variable booleana:", bool_variable)

# Alugnas funciones del sistema
print(len(string_variable))

# Variables en una sola línea
nombre, apellido, alias, edad = "Johan", "Moreno", "El Moreno", 19
print("Mi nombre es", nombre, ". Mi apellido es", apellido, ". Me dicen", alias, "y tengo", edad, "años")

# Inputs
"""
nombre = input("¿Cuál es tu nombre?: ")
edad = input("¿Cuántos años tienes?: ")
print(nombre)
print(edad)
"""

# Cambiamos su tipo de dato
nombre = 19
edad = "Johan"
print(nombre)
print(edad)

# ¿Forzamos el tipo? SPOILER: NO!!
direccion: str = "Mi dirección"
direccion = 32
print(type(direccion))