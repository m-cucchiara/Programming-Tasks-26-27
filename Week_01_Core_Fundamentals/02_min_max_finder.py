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
    pass

def find_min_max(values):
    min_value = number[0]
    max_value = 0
    for number in values:
        if number <= min_value:
            min_value = number
        elif number > max_value:
            max_value = number

    return min_value, max_value




listOfNumbers = input("Enter a list of numbers seperated by commas: ")
listOfNumbers = listOfNumbers.split(",")

find_min_max(listOfNumbers)
if __name__ == "__main__":
    main()
