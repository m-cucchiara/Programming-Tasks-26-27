"""
TASK: 03 Array Reversal

# Array Reversal
Create a program that:
- Generates a list of random integers.
- Reverses the list manually (no slicing or .reverse).
- Includes a function `reverse_list(values)` that returns a new reversed list.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""
import random
def main():
    # TODO: Write demonstration/testing code
    # If you want to delete all the code here and work just with a blank file go ahead, remember anything under the if __name__=="__main__":
    # will only run if this module is being run directly. So used this subprocedure to carry out testing if it is going to be an imported file.

    # Constructs list
    list = []
    amount = random.randint (1, 50)
    for i in range(0, amount):
        number = random.randint(1, 100)
        list.append(number)

    return list

def reverse_list(values):

    # Reverses list by appending values from previous list to new list from end to start
    newList = []
    amount = len(list)

    for i in range (0, amount):
        newPos = amount - i
        newList.append(list[newPos - 1])

    return newList

if __name__ == "__main__":
    list = main()
    print(list)

print(reverse_list(list))