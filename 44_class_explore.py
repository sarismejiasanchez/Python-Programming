# Exercise: exploring classes and objects
"""
En esta lectura, explorará el comportamiento de funciones, objetos y clases en Python y cómo funciona el flujo de ejecución de diferentes sentencias de programa para permitir una mejor comprensión.

Realizará modificaciones menores en el código dado para observar cómo cambia la salida.
"""

print("Hello World!")

class A:
    """
    Class A:
    A simple class that demonstrates initialization and a method to manipulate an attribute.
    """

    def __init__(self, c):
        """
        Constructor for class A.

        Args:
            c (int): An integer value to initialize the attribute `c`.

        Prints:
            A message indicating that the constructor of class A is being executed.
        """
        print("---------Inside class A----------")
        self.c = c
        print("Print inside A.")

    def alpha(self):
        """
        Method alpha:
        Increments the value of the attribute `c` by 1.

        Returns:
            int: The incremented value of `c`.
        """
        c = self.c + 1
        return c

print(dir(A)) # Prints the list of attributes and methods of class A

# Creating an instance of class A
# The following code demonstrates how to create an instance of class A
# and call its method `alpha`.

print("Instantiating A..")  # Indicates the creation of an instance of class A
a = A(1)  # Creates an instance of class A with the attribute `c` initialized to 1
print(a.alpha())  # Calls the method `alpha` on the instance `a` and prints the result

# Calling the method `alpha` on the instance `a`
# The following code demonstrates how to call the method `alpha` on an instance of class A
# and print the result.

class B:
    """
    Class B:
    A simple class that demonstrates initialization and interaction with an instance of class A.
    """

    def __init__(self, a):
        """
        Constructor for class B.

        Args:
            a (A): An instance of class A passed to initialize the attribute `a`.

        Prints:
            A message indicating that the constructor of class B is being executed.
        """
        print("---------Inside class B----------")
        self.a = a
    
    # Note: The following lines are executed when the class B is defined,
    # not when an instance of B is created. They use the global 'a' instance of A.
    print(a.alpha())
    d = 5
    print(d)
    print(a)
    
# Creating an instance of class B
# The following code demonstrates how to create an instance of class B
# using an instance of class A as an argument.

print("Instantiating B..")  # Indicates the creation of an instance of class B
b = B(a)  # Creates an instance of class B with the attribute `a` initialized to the instance of class A
print("Instance of B created:", b)  # Prints the created instance of class B


# Step 1: run the code and observe its output. Take note of each line in the result and how it differs from what you expected.
"""
Hello World!
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'alpha']
Instantiating A..
---------Inside class A----------
Print inside A.
2
2
5
<__main__.A object at 0x7631de1332c0>
Instantiating B..
---------Inside class B----------
Instance of B created: <__main__.B object at 0x7631ddf339e0>
"""

# Step 2: comment out lines #13, 14, 21, 24, 27, and 28. Run the code again.
"""
# 1. class A:
# 2.     def __init__(self, c):
# 3.         print("---------Inside class A----------")
# 4.         self.c = c
# 5.     print("Print inside A.")
# 6.
# 7.     def alpha(self):
# 8.         c = self.c + 1
# 9.         return c
# 10.
# 11. print(dir(A))
# 12. print("Instantiating A..")
# 13. # a = A(1)
# 14. # print(a.alpha())
# 15.
# 16. class B:
# 17.     def __init__(self, a):
# 18.         print("---------Inside class B----------")
# 19.         self.a = a
# 20.
# 21.     # print(a.alpha())
# 22.     d = 5
# 23.     print(d)
# 24.     # print(a)
# 25.
# 26. print("Instantiating B..")
# 27. # b = B(a)
# 28. # print(a)

Output of the code after commenting out the specified lines:

Hello World!
Print inside A.
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'alpha']
Instantiating A..
5
Instantiating B..

Aunque haya comentado la creación de instancias para ambas clases A y B, la salida sigue mostrando “Print inside A” y “Print inside B” y también el valor de la variable "d", que es 5. ¿Cómo es eso posible?

Es porque las sentencias dentro de un cuerpo de clase se ejecutan independientemente de la creación de la instancia. También verá cómo la sentencia "print" “Inside class A”, que está dentro del constructor, no se ejecuta porque está dentro de una función. 

El valor de d=5 que se imprime demuestra que el espacio de nombres y el alcance de la variable se determinan por el intérprete antes de crear cualquier instancia de la clase o llamar a cualquier función dentro de ella. Si observa la lista que obtiene llamando a la función "dir()", notará que la última entrada es la función "alpha()" agregada al espacio de nombres de A.
"""

# Step 3: now uncomment lines 21 and 24.
"""
Hello World!
Print inside A.
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'alpha']
Instantiating A..
Traceback (most recent call last):
  File "/workspaces/Python-Programming/test.py", line 16, in <module>
    class B:
  File "/workspaces/Python-Programming/test.py", line 21, in B
    print(a.alpha())
          ^
NameError: name 'a' is not defined. Did you mean: 'A'?


Si ejecuta el código en este punto, arrojará un error, "NameError: name 'a' is not defined" (Nombre de error: el nombre "a" no está definido). Tome nota de cómo pasó el objeto a un constructor de clase B y el código aún funcionó bien antes. Solo cuando intentó 'utilizar' el objeto "a", obtuvo un error porque no se ha creado una instancia. En otras palabras, Python aún no sabe lo que significa 'a'. Lo mismo sucederá si se quita el comentario junto a la línea 28. 
"""

# To make the code work, remove the # in front of line 14, 14 and run it again.
"""
Print inside A.
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'alpha']
Instantiating A..
---------Inside class A----------
2
2
5
<__main__.A object at 0x74dbd84279b0>
Instantiating B..
"""

# Step 4: uncomment lines 27 and 28.

"""
Print inside A.
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'alpha']
Instantiating A..
---------Inside class A----------
2
2
5
<__main__.A object at 0x7872024e7950>
Instantiating B..
---------Inside class B----------
<__main__.A object at 0x7872024e7950>



La variable "c" de la clase A se modifica sobre el objeto "a" dentro de la clase B. Aunque la instancia de clase B aún no se crea, el valor de "a.c" se actualiza, incluso fuera de la clase, como lo demuestra la línea final en la salida que muestra que el resultado es 2.
"""

# Step 5: finally, remove all remaining comments and run the code once more.

"""
A continuación, algunas observaciones:

Cuando intente imprimir el 'objeto' de la clase A como en las líneas 21 y 28, obtendrá la dirección del objeto en lugar de los contenidos.

Observe cómo la dirección del objeto es la misma tanto dentro de la clase B como en el ámbito global del programa. Sigue siendo la misma independientemente de donde se la llame.

La función "alpha()" se llama dos veces en el programa, pero usted sigue obteniendo el resultado como 2 cada vez y no 3. Eso se debe a que el valor se actualiza temporalmente y no se asigna a nada.

Revise los elementos sobre clases, llamadas a funciones y alcance en caso de confusión.
"""
