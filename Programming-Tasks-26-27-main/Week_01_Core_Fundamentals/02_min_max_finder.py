"""
TASK: 02 Min Max Finder

# Min/Max Finder
Write a program that:
- Accepts a list of integers.
- Manually finds the min and max (no built-in min/max).
- Includes a function `find_min_max(values)` returning `(min_value, max_value)`.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
    # TODO: Write demonstration/testing code
    # If you want to delete all the code here and work just with a blank file go ahead, remember anything under the if __name__=="__main__":
    # will only run if this module is being run directly. So used this subprocedure to carry out testing if it is going to be an imported file.
    listOfNumbers = input("Enter a list of numbers seperated by commas: ")
    listOfNumbers = listOfNumbers.split(",")

    max = find_min_max(listOfNumbers)

    print("The minimum value is: ", max[0])
    print("The maximum value is: ", max[1])

def find_min_max(values):
    min_value = values[0]
    max_value = 0
    for number in values:
        if int(number) <= int(min_value):
            min_value = int(number)
        elif int(number) > max_value:
            max_value = int(number)

    return min_value, max_value


if __name__ == "__main__":
    main()
