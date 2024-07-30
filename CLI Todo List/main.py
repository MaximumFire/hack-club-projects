"""
have a main menu with following options: (items are listed as part of the menu)
- add item
- edit item
- remove item
- quit
"""

items = []

def list_items():
    if len(items) == 0:
        return
    print("Items:")
    for i, item in enumerate(items):
        print(f"[{i}] - {item}")
    print()

def add_item():
    new_item = input("Enter a new todo item: ")
    items.append(new_item)
    print("Item added")
    print()

def edit_item():
    i = int(input("Enter the code for the item to edit: "))
    new_item = input("Enter the new text for that item: ")
    items[i] = new_item
    print("Item edited")
    print()

def remove_item():
    i = int(input("Enter the code for the item to remove: "))
    items.pop(i)
    print("Item removed")
    print()

def main_menu():
    print("--Main Menu--")
    list_items()
    print("(1) - Add item")
    print("(2) - Edit item")
    print("(3) - Remove item")
    print("(4) - Quit")
    a = int(input("Choose an option: "))
    match a:
        case 1:
            add_item()
        case 2:
            edit_item()
        case 3:
            remove_item()
        case 4:
            exit(0)
        case _:
            return
        
if __name__ == "__main__":
    while True:
        main_menu()