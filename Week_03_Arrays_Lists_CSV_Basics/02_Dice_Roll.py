"""
TASK: 02 Dice Roll

# Skills: RNG, Loops
Simulate rolling a six-sided die X number of times:
Print each roll, store all values in a list of updated totals for each number (56 ones for example):
Allow the user to print:
- Totals for each side
- average dice roll
- Counts for each of the 6 sides
- Extend (look up how to use mathplotlib and produce a bar graph for all of the statistics)

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""
import random
import matplotlib.pyplot as plt
import numpy as np

def main():
    # TODO: Write demonstration/testing code
    # If you want to delete all the code here and work just with a blank file go ahead, remember anything under the if __name__=="__main__":
    # will only run if this module is being run directly. So used this subprocedure to carry out testing if it is going to be an imported file.
    rollCount = int(input("Enter how many times the dice should roll: "))
    list = dice_roll(rollCount)
    print(list)

    average = average_calc(list, rollCount)
    print(average)

    display_bar_graph(list)

def dice_roll(rollCount):
    list = [0,0,0,0,0,0]
    for i in range(rollCount):
        sideRolled = random.randint(1,6)
        list[sideRolled - 1] += 1


    return list

def average_calc(list, totalRoll):
    total = 0

    for i in range(1,6):
        total += list[i] * i

    average = total / totalRoll

    return average

def display_bar_graph(list):
    x = np.array(["1", "2", "3", "4", "5", "6"])
    y = np.array(list)

    plt.bar(x,y)
    plt.show()

if __name__ == "__main__":
    main()
