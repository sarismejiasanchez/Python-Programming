# CONVERT DATA TYPES

# Implicit Type Casting
# La realiza automáticamente el compilador para evitar la pérdida de datos
a = 10
b = 20.5
c = a + b
print(c) # 30.5

print(10 == 10.0) # True
print(10 + 10.0) # 20.0 cuando Python ejecuta operaciones con enteros y flotantes, convierte implícitamente el tipo de enteros en un flotante y luego completa la operación.

# Type() FUNCTION
# Esta función devuelve el tipo de dato de un objeto
print(type(10 + 10.0)) # <class 'float'>

# Explicit Type Casting
# str() FUNCTION
# Esta función se puede utilizar para convertir el valor proporcionado en una String
print(str(11)) # '11'

# int() FUNCTION
# Esta función se puede utilizar para convertir el valor proporcionado en un int
print(int(20.5)) # 20

user_num_1 = "5"
user_num_2 = "5"
user_sum = user_num_1 + user_num_2
print(user_sum) # 55

user_sum = int(user_num_1) + int(user_num_2)
print(f"The sum of {int(user_num_1)} and {int(user_num_2)} is {user_sum}") # The sum of 5 and 5 is 10

# float() FUNCTION
# Esta función se puede utilizar para convertir el valor proporcionado en un float
print(float('50.4')) # 10.0

user_sum = float(user_num_1) + float(user_num_2)
print(f"The sum of {float(user_num_2)} and {float(user_num_2)} is {user_sum}") # The sum of 5.0 and 5.0 is 10.0

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

# COMPARISON OPERATORS
a = 10
b = 20

print(a == b)   # False
print(a != b)   # True
print(a < b)    # True
print(a > b)    # False
print(a <= b)   # True
print(a >= b)   # False

print(10 == 10) # True
print(10 == 10.0) # True    # Implicit Type Casting
