"""
TASK: 01 Bubble Sort

# Bubble Sort
Implement Bubble Sort on any size list:
- Do not use built-in sort()
- Count swaps
- Extend by

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
    # TODO: Write demonstration/testing code
    # If you want to delete all the code here and work just with a blank file go ahead, remember anything under the if __name__=="__main__":
    # will only run if this module is being run directly. So used this subprocedure to carry out testing if it is going to be an imported file.
    numbers = [42, 7, 19, 3, 88, 12, 1, 95, 23, 14] # example list
    numbers, count = bubble_sort(numbers)

    print("Sorted list: ", numbers)
    print("Number of swaps: ", count)


def bubble_sort(numbers):
    count = 0

    for j in range(len(numbers)):
        for i in range(len(numbers) - 1):
            prev = numbers[i]
            next = numbers[i + 1]
            if prev > next:
                count += 1
                numbers[i] = next
                numbers[i + 1] = prev

    return numbers, count




if __name__ == "__main__":
    main()