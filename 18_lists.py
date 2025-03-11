# LISTS
# Lists are a sequence of one or more different or similar data types.
# A list in Python is essentially a dynamic array that can hold any datatype.

list1 = [1, 2, 3, 4, 5] # This is a list of integers
list2 = ["A", "B", "C", "D"] # This is a list of strings
list3 = ["Hello", 1, True, 40.22] # This is a list of mixed data types

# One thing to keep in mind with lists is that they are based on an index and the index always starts at 0.
# So the first element in a list is at index 0, the second element is at index 1 and so on.

# Accessing the third element in list1
print(f"Third element in list1 is {list1[2]}")

# Lists can contain other lists as well
list4 = ["Hello", list1, "Goodbye"]
print(f"list4: {list4}")
print(f"The list inside list4 is {list4[1]}")

# Print the list
print(list2) # This will print the list as it is
print(*list2) # This will print each element in the list separated by a space
print(*list2, sep = " | ") # This will print each element in the list separated by a pipe

# Adding elements to a list

# Insert: This method is used to insert an element at a specific index in the list
list2.insert(len(list2), 6) # This will insert the number 6 at the end of the list
print(f"Insert: {list2}")

list2.insert(2, "Hello") # This will insert the string "Hello" at index 2
print(f"Insert: {list2}")

# Append: This method is used to add an element at the end of the list without specifying the index
list2.append("World") # This will add the string "World" at the end of the list
print(f"Append: {list2}")

# Extend: This method is used to add multiple elements to the end of the list
list2.extend([7, 8, 9, "end"]) # This extends the list by adding the elements in the list [7, 8, 9, "end"]
print(f"Extend: {list2}")

# Removing elements from a list
list2.pop() # This will remove the last element "end" from the list
print(f"Pop: {list2}")

list2.pop(2) # This will remove the element at index 2 "Hello" from the list
print(f"Pop with index: {list2}")

del list2[1] # This will remove the element at index 1 "B" from the list
print(f"Del: {list2}")

# Remove: This method is used to remove the first occurrence of a specific element from the list
# Adding the element "C" back to the list
list2.append("C")
print(f"Add C again to be list: {list2}")
list2.remove("C") # This will remove the first occurrence of the element "C" from the list

# In this case, it removes the first occurrence of the element 'C' located at index 2, but the element 'C' at the end is preserved.
print(f"Remove: {list2}")

# Iterating through a list
print(f"Iterating through a list: {list3}...")
for element in list3:
    print(element)

print(f"Iterating through a list: {list3} with index...")
for index, element in enumerate(list3):
    print(f"Index: {index}, Element: {element}")
