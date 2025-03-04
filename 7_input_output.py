# INPUT FUNCTION
# Esta función busca el dispositivo de entrada predeterminado, su teclado, y captura el valor. 
# Este valor se puede asignar o utilizar.
email = input("Please enter your email address: ")
print(email)

num1 = input("Please enter a first number: ")
num2 = input("Please enter a second number: ")
print(num1, num2)

# len() FUNCTION
# Esta función devuelve la longitud o el recuento de los elementos contenidos en la estructura en la que se aplica. Puede ser una cadena, una matriz, una lista, una tupla, un diccionario o cualquier secuencia.
name = "John"
print(len(name)) # 4

# print() FUNCTION
# Esta función busca el dispositivo de salida predeterminado, su terminal, y muestra el valor que se le pasa.
print("Hello")

# print arguments comma separated
print(1, 2, 3)

# arithmetics
print(1 + 3)

# string concatenation
name = "John"
print("Hello " + name)

# string formatting

# Palabras clave como argumentos reservados
# objects: valores impresos por pantalla
# sep: separador entre los objetos
# end: qué se imprime al final de la cadena
# file: un archivo que especifica dónde se imprimen los valores, por defecto es "STD out" la consola
# flush: expresion booleana que indica si se debe vaciar el buffer de salida. Este mueve los datos de una memoria temporal a una memoria permanente.

print("Hello", "you!", sep = ", ") # Hello, you!
print("Hello", "you!", end = " :)") # Hello you! :)
print("Hello", "you!", file = open("output.txt", "w")) # Generate the output.txt file with Hello you! as its content.
print("Hello", "you!", flush = True) # Hello you!

# Direct formatting
a = 10
b = 5
ans = a + b
print("Adding the value of {} and {} = {}".format(a, b, ans)) # Adding the value of 10 and 5 = 15

# Output formatting
print("I like {0} more than {1}".format("oranges", "grapes")) # I like oranges more than grapes
print("I like {1} more than {0}".format("oranges", "grapes")) # I like grapes more than oranges

# f-string
name = "John"
surname = "Doe"
print(f"Hello {name} {surname}") # Hello John Doe
