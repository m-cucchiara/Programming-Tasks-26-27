"""
TASK: 05 Shopping List

# Skills: Loops, lists
Allow the user to add itemds to a shopping list until they type DONE
When they type DONE, print the list and ask if they want to edit any item.
They should select an item by number and allow them to ammend the item.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
    # TODO: Write demonstration/testing code
    # If you want to delete all the code here and work just with a blank file go ahead, remember anything under the if __name__=="__main__":
    # will only run if this module is being run directly. So used this subprocedure to carry out testing if it is going to be an imported file.
    shoppingList = []
    shopping_list_append(shoppingList)

def shopping_list_append(shoppingList):
    choice = input("Enter choice (type Done to exit): ")
    while choice.upper() != "DONE":
        choice = input("Enter choice (type Done to exit): ")
        shoppingList.append(choice)

    if choice.upper() == "DONE":
        shopping_list_edit(shoppingList)

def shopping_list_edit(shoppingList):
    print(shoppingList)
    editRequest = input("Would you like to edit your shopping list? (y/n): ")

    while editRequest != "n":
        index = int(input("Enter which position you would like to edit: "))
        itemChange = input("Enter the name of new item: ")
        shoppingList[index] = itemChange
        print(shoppingList)
        editRequest = input("do you still need to change anything? (y/n): ")





if __name__ == "__main__":
    main()
