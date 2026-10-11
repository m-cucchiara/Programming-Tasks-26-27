"""
TASK: 04 Linear Search

# Linear Search
Implement a linear search algorithm:
- Ask the user for a target value.
- Search a generated random list.
- Return the index or -1.
- Include `linear_search(values, target)`.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""
import random
list = []

def main():
    # TODO: Write demonstration/testing code
    # If you want to delete all the code here and work just with a blank file go ahead, remember anything under the if __name__=="__main__":
    # will only run if this module is being run directly. So used this subprocedure to carry out testing if it is going to be an imported file.

    # Constructs list with a max of 50 items
    amount = random.randint(1, 100)

    for i in range(1, amount):
        number = random.randint(1, 100)
        list.append(number)

    return list

def linear_search(values, target):
    found = False
    index = 0

    for number in list:
        index = index + 1
        if number == target:
            found = True
            break



    return index, found




if __name__ == "__main__":
    print(main())

searchTarget = int(input("Enter a number to search: "))

found = linear_search(list, searchTarget)

if found[1] == True:
    print("Item found on position number", found[0])

else:
    print("Item not found")