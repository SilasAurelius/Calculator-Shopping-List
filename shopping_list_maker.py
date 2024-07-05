shopping_list = []

def add_item(item):
    shopping_list.append(item)
    print(f"{item} added to list.")
    
def remove_item(item):
    shopping_list.remove(item)
    print(f"{item} removed from list.")
    
def print_list():
    print("Current shopping list:")
    for i, item in enumerate(shopping_list, 1):
        print(f"{i}. {item}")
 
while True: 
	manage_list = input("Type: + to add, - to remove, c to check list, q to quit:: ")
	if manage_list == "+":
		item = input("Input item to add: ")
		add_item(item)
	elif manage_list == "-":
		item = input("Input item to remove: ")
	elif manage_list == "c":
		print_list()
	else:
		print(f"Final List: {print_list(shopping_list)}")
		break
    
     
 