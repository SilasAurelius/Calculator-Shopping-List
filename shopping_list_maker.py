#Task 1: Write a function that lets the user add items to a list.
shopping_list = []

def add_item(item):
    global shopping_list
    shopping_list.append(item)
    print(f"{item} added to list.")
# Task 2: Include a function to remove items from the list.    
def remove_item(item):
    global shopping_list
    shopping_list.remove(item)
    print(f"{item} removed from list.")
# Task 3: Add a function that prints out the entire list in a formatted way.    
def print_list():
    print("Current shopping list:")
    for i, item in enumerate(shopping_list, 1):
        print(f"{i}. {item}")
 
while True: 
    manage_list = input("Type: + to add, - to remove, q to quit:: ")
    if manage_list == "+":
        item = input("Input item to add: ")
        add_item(item)
    elif manage_list == "-":
        item = input("Input item to remove: ")
        remove_item(item)
    elif manage_list == "q":
        print_list()
        print("Exiting program.")
        break
    else:
        print("Invalid input. Please try again.")
