"""
TASK: 02 Binary Search Tester

# Binary Search Tester
Generate a sorted list. Implement:
- iterative binary search
- recursive binary search
Then benchmark them with random inputs.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
    # TODO: Write demonstration/testing code
    # If you want to delete all the code here and work just with a blank file go ahead, remember anything under the if __name__=="__main__":
    # will only run if this module is being run directly. So used this subprocedure to carry out testing if it is going to be an imported file.
    list = [1,2,3,4,5,6,7,8,9,10]
    searchTerm = int(input("Enter number: "))

    iterative = iterative_bubble_sort(list, searchTerm)
    recursive = recursive_bubble_sort(list, searchTerm, iterative)


    if iterative[0] == True:
        print("Found at index, ", iterative[1])
    else:
        print("Index not found")

def iterative_bubble_sort(list, searchTerm):
    range1 = 0
    range2 = len(list)
    newVal = range2 // 2
    found = False

    while found != True:
        newVal = newVal // 2

        if list[newVal] == searchTerm:
            found = True
        else:
            if searchTerm > list[newVal]:
                range1 += newVal
            else:
                range2 -= newVal

            newVal = range1 + range2


    return found, newVal

def recursive_bubble_sort(list, searchTerm, iterative):
    range1 = 0
    range2 = len(list)
    newVal = range2 // 2

    if list[newVal] == searchTerm:
        return True, newVal
    else:
        return iterative

if __name__ == "__main__":
    main()

