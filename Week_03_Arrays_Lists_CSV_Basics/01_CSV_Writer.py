"""
TASK: 01 Csv Writer

# Skills: CSV writing
CAsk the user for:
- Name
- age
- favourite colour
- anything you want
Append this to a CSV file (Extend: allow user to choose to edit the file and read the file)

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
    # TODO: Write demonstration/testing code
    # If you want to delete all the code here and work just with a blank file go ahead, remember anything under the if __name__=="__main__":
    # will only run if this module is being run directly. So used this subprocedure to carry out testing if it is going to be an imported file.
    choice = 0
    while choice >= 1 or choice <= 2:
        choice = int(input("Enter 1 to edit, 2 to read the file, any other number to exit: "))
        if choice == 1:
            csv_writer()
        elif choice == 2:
            file_show()
        else:
            break

def csv_writer():
    file = open("file.txt", "a")
    name = input("Enter name: ")
    age = input("Enter age: ")
    favColor = input("Enter favorite color: ")
    extra = input("Write anything else (leave blank if nothing): ")

    setup = str(name + "," + age + "," + favColor)

    file.write(setup)

    if extra != "":
        file.write(str("," + extra))

    file.write("\n")

    file.close()

def file_show():
    try:
        file = open("file.txt", "r")
    except:
        print("Could not open file.")

    for line in file:
        print(line)

    file.close()


if __name__ == "__main__":
    main()
