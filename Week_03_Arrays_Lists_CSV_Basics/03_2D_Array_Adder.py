"""
TASK: 03 2D Array Adder

# 2D Array Added
Create a 2D array and allow user to:
- Append new values in
- read all current values
- delete a chosen entry

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
    # TODO: Write demonstration/testing code
    # If you want to delete all the code here and work just with a blank file go ahead, remember anything under the if __name__=="__main__":
    # will only run if this module is being run directly. So used this subprocedure to carry out testing if it is going to be an imported file.
    array = []
    choice = -1

    while choice != 0:
        choice = int(input("Enter 1 to append values, 2 to read current entries, 3 to delete an entry, and any other number to end: "))
        if choice == 1:
            value_appender(array)
        elif choice == 2:
            array_reader(array)
        elif choice == 3:
            del_entry(array)
        else:
            break



def array_reader(array):
    for record in array:
        print(record)

def value_appender(array):
    record = []
    items = int(input("Enter how many items you want to input: "))

    for i in range(items):
        value = input("Enter value: ")
        record.append(value)

    array.append(record)

    record = []

def del_entry(array):
    recordIndex = int(input("Enter the index for the record you want to delete: "))
    try:
        del array[recordIndex]
    except:
        print("Index is outside range")

if __name__ == "__main__":
    main()
