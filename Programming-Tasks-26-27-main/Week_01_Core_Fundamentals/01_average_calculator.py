""" TASK: 01 Average Calculator

# Average Calculator
Write a Python program that:
- Prompts the user for a list of numbers.
- Stores them in a 1D list.
- Calculates the mean *without using built-in statistics libraries*.
- Includes input validation.
- Implements a reusable function: `calculate_average(values)`.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""
numberList = []

def main():
    amount = int(input("Enter how many numbers you want to enter: "))
    
    for i in range(0, amount):
        number = int(input("Enter a number: "))
        numberList.append(number)

def calculate_average(values):
    total = 0
    for numbers in values:
        total = total + numbers

    meanNum = total / amount
    return meanNum





if __name__ == "__main__":
    main()

print(calculate_average(numberList))

