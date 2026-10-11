"""
TASK: 03 Grid Path Counter

# Grid Path Counter - https://bk2coady.medium.com/daily-coding-problem-62-bfe0e398247b`
Given an NxM grid:
- Count paths using recursion
- Count paths using iteration
Movement allowed: RIGHT or DOWN only.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
    # TODO: Write demonstration/testing code
    # If you want to delete all the code here and work just with a blank file go ahead, remember anything under the if __name__=="__main__":
    # will only run if this module is being run directly. So used this subprocedure to carry out testing if it is going to be an imported file.
    m = int(input("Enter m: "))
    n = int(input("Enter n: "))

    grid = grid_maker(m, n)
    print("Number of paths: ", iterative_solution(m, n, grid))

def grid_maker(m, n):
    grid = []
    row = []
    for i in range(m + 1):
        for j in range(n + 1):
            if j == 0 or i == 0:
                row.append(1)
            else:
                row.append(0)


        grid.append(row)
        row = []

    return grid


def iterative_solution(m, n, grid):
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if i == m:
                sumOfNumbers = grid[i][j - 1]
            elif j == m:
                sumOfNumbers = grid[i - 1][j]
            else:
                sumOfNumbers = grid[i][j - 1] + grid[i - 1][j]


            grid[i][j] = sumOfNumbers

    return grid[m - 1][n - 1]



if __name__ == "__main__":
    main()
