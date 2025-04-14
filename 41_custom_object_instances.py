# CUSTOM OBJECT INSTANCES

class Recipe:
    """
    Recipe class demonstrates the use of the __new__ and __init__ methods in Python.

    Methods:
        __new__(cls) -> 'Recipe':
            Creates and returns a new instance of the Recipe class.
            This method is called before __init__ and is used to control object creation.

        __init__(self) -> None:
            Initializes the instance of the Recipe class.
            This method is called after __new__ and is used to set up the object's attributes.
    """

    def __init__(self, dish, items, time) -> None:
        self.dish = dish
        self.items = items
        self.time = time
        
    def contents(self):
        """
        Returns a string representation of the Recipe instance.

        Returns:
            A string containing the dish name, items, and time.
        """
        print(f"The {self.dish} contains {self.items} and takes {self.time} minutes to prepare.")
        
# Example usage
pizza = Recipe("Pizza", ["cheese", "bread", "tomato sauce"], 45)
pasta = Recipe("Pasta", ["penne", "sauce"], 55)

# Accessing attributes
print(pizza.items)
print(pasta.items)

# Calling the contents method
print(pizza.contents())
print(pasta.contents())

# You have written the following Python code that uses a class:
class Bicycle:

    def __init__(self, size, gears):
        self.size = size
        self.gears = gears

# print(roadBike.gears)
# The result will be "gears". True or false?

# False. In this code, no instance of a RoadBike object has been created, so running this code would result in an error. 

# EXERCISE: INSTANTIATE A CUSTOM OBJECT

# Define class MyFirstClass
class MyFirstClass:
    print("Who wrote this?")
    # Define string variable called index
    index = "Author-Book"
    
    # Define function hand_list()
    def hand_list(self, philosopher, book):
        print(MyFirstClass.index) # Author-Book
        print(f"{philosopher} wrote the book: {book}")
        
# Create an instance of MyFirstClass
whodunnit = MyFirstClass()

# Call function handlist()
# print(whodunnit.hand_list("Plato", "The Republic"))
print(whodunnit.hand_list("Sun Tzu", "The Art of War"))

# How would you modify the code to include a "year" of publication in the output?
class MyFirstClass():
    print("Who wrote this?")
    index = "Author-Book"
    def hand_list(self, philosopher, book, year):
        print(MyFirstClass.index)
        print(f"{philosopher} wrote the book: {book} in {year}")
whodunnit = MyFirstClass()
whodunnit.hand_list("Sun Tzu", "The Art of War", "5th century BC")
# def hand_list(self, philosopher, book, year):
# print(f"{philosopher} wrote the book: {book} in {year}")
# whodunnit.hand_list("Sun Tzu", "The Art of War", "5th century BC")
