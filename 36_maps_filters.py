# MAP AND FILTER
# Process a list with the map and filter functions

menu = ["espresso", "mocha", "latte", "cappuccino", "cortado", "americano"]

# Find coffees that start with 'c'
def starts_with_c(coffee):
    if coffee[0] == "c":
        return coffee

# Map the function to the menu
# Maps take all objects in a list and applies a function to each object.
map_coffees = map(starts_with_c, menu)
print(map_coffees) # <map object at 0x7fc78c6f7b80>
for coffee in map_coffees:
    if coffee != None:
        print(coffee)

# Filter the function to the menu
# Filters do same, but take the results and creates a new list with only the objects that returned True.
filter_coffees = filter(starts_with_c, menu)
print(filter_coffees) # <filter object at 0x7fc78c6f7c10>
for coffee in filter_coffees:
    print(coffee)