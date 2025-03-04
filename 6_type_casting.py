# CONVERT DATA TYPES

# Implicit Type Casting
# La realiza automáticamente el compilador para evitar la pérdida de datos
a = 10
b = 20.5
c = a + b
print(c) # 30.5

# Explicit Type Casting
# str() FUNCTION
# Esta función se puede utilizar para convertir el valor proporcionado en una String
print(str(11)) # '11'

# int() FUNCTION
# Esta función se puede utilizar para convertir el valor proporcionado en un int
print(int(20.5)) # 20

# float() FUNCTION
# Esta función se puede utilizar para convertir el valor proporcionado en un float
print(float('50.4')) # 10.0

# Type Conversion Functions
# ord() FUNCTION
# Esta función devuelve el número entero que representa el carácter Unicode proporcionado

# hex() FUNCTION
# Convierte un entero en una cadena hexadecimal

# oct() FUNCTION
# Devuelve una cadena octal de un entero

# tuple() FUNCTION

# set() FUNCTION

# list() FUNCTION

# dict() FUNCTION

# Question:
# Una empresa quiere determinar la edad general de sus clientes. Usted los ayuda escribiendo un programa que utilice el número de identificación de un cliente (7512171283423) para determinar su edad. Pero el conjunto de datos que se le proporciona tiene los números de identificación guardados como cadenas. ¿Qué función tipográfica puede utilizar para resolver el problema?

id_number = '7512171283423'
print(int((id_number))) # 7512171283423