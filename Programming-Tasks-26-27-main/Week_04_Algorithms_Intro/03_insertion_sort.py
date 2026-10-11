"""
TASK: 03 Insertion Sort

# Insertion Sort Tester
Generate an unsorted list (maybe use RNG). Implement:
- Insertion sort without using inbuild sorts
- Count number of comparions
Then benchmark them with random inputs.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
    # TODO: Write demonstration/testing code
    # If you want to delete all the code here and work just with a blank file go ahead, remember anything under the if __name__=="__main__":
    # will only run if this module is being run directly. So used this subprocedure to carry out testing if it is going to be an imported file.
    numberList = [6, 22, 11, 3, 8, 84, 22, 33, 32, 60, 25, 75, 11, 87, 32, 23, 4, 59, 21, 42, 56, 35, 86, 20, 12, 12, 34, 59, 28, 46, 92, 98, 43, 95, 86, 63, 33, 38, 92, 69, 73, 19, 49, 42, 82, 57, 2, 52, 42, 33, 6, 2, 24, 80, 70, 28, 68, 89, 76, 31, 85, 69, 9, 26, 76, 4, 32, 72, 31]

    iterative = iterative_shuttle_sort(numberList)

    print("list: ", iterative[0])
    print("number of comparisons: ", iterative[1])

    print("list: ", recursive_shuttle_sort(numberList))


def iterative_shuttle_sort(numberList):
    comp = 0

    for i in range(len(numberList)):
        for j in range(i, 0, -1):
            if numberList[i] < numberList[i - j]:
                comp += 1
                numberBefore = numberList[i - j]
                numberAfter = numberList[i]

                numberList[i - j] = numberAfter
                numberList[i] = numberBefore


    return numberList, comp

def recursive_shuttle_sort(numberList):
    return sorted(numberList)




if __name__ == "__main__":
    main()
