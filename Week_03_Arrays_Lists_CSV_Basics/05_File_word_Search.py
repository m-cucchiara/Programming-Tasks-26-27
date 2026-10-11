"""
TASK: 05 File Word Search

# Skills: File reading, loops, Data mining
Ask user for a filename and a search term. https://sherlock-holm.es/ascii/ is a site that has the entire collection of Sherlock Holmes
Load the file and count how many lines contain the search term

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
    # TODO: Write demonstration/testing code
    # If you want to delete all the code here and work just with a blank file go ahead, remember anything under the if __name__=="__main__":
    # will only run if this module is being run directly. So used this subprocedure to carry out testing if it is going to be an imported file.
    file = open("cano.txt", "r")
    count = search_system(file)

    print("Your search term appeared", count, "times")

def search_system(file):
    count = 0
    searchItem = input("Enter search term: ")
    for line in file:
        line = line.strip()
        line = line.strip(" ")
        line = line.split(" ")

        for word in line:
            if word == searchItem:
                count += 1
                break

    return count




if __name__ == "__main__":
    main()
