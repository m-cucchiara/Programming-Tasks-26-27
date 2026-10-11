"""
TASK: 03 Contact Book

# Store contacts in a text file, each line containing
name,phone,email
Program must allow:
- Add contact
- Search contact (sequential search)
- Display all

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
    # TODO: Write demonstration/testing code
    # If you want to delete all the code here and work just with a blank file go ahead, remember anything under the if __name__=="__main__":
    # will only run if this module is being run directly. So used this subprocedure to carry out testing if it is going to be an imported file.

    fileName = "contacts.txt"

    print("1 | Add contact")
    print("2 | Search contact")
    print("3 | Display all")
    print("4 | Exit program")

    choice = str(input("Enter choice: "))

    if choice >= "1" and choice <= "3": # only for choices that allows interaction with the file (1-3)
        if choice == "1":
            add_contact(fileName)
        elif choice == "2":
            search_contact(fileName)
        elif choice == "3":
            display_all(fileName)

        print("Operation sucessful!")
        main()

    elif choice == "4":
        print("Exited program")
    else:
        print("Invalid input. Try again")
        main()  # recurses back to main() if theres an invalid input

def add_contact(fileName):
    file = open(fileName, "a")

    # asks user for data
    name = input("Enter name: ")
    phoneNumber = input("Enter phone number: ")
    eMail = input("Enter email: ")

    # data gets inputted into the file
    file.write(name)
    file.write(",")
    file.write(phoneNumber)
    file.write(",")
    file.write(eMail)
    file.write("\n")

    file.close()

def search_contact(fileName):
    file = open(fileName, "r")

    # asks user what index they want to search in
    print("0 | Search by name")
    print("1 | Search by number")
    print("2 | Search by email")

    choice = int(input("Enter choice: "))
    searchTerm = input("Enter search term: ")

    try:
        if choice >= 0 and choice <= 2:
            for line in file:
                line = line.strip()
                line = line.split(",")

                if searchTerm in line[choice]: # checks if the search term is in that index
                    print("Result found!")
                    print("Name: ", line[0])
                    print("Phone number: ", line[1])
                    print("Email: ", line[2])   # if a result is found, it outputs the contents of the line in a readable format

        else:
            print("Invalid input, try again.")  # if choice is outside the range it sends this message
            search_contact(fileName) # then recurses back to this subprogram

    except ValueError:
        print("Invalid input, try again") # if theres a valueError it sends this message
        search_contact(fileName) # then recurses back to this subprogram


def display_all(fileName):
    file = open(fileName, "r")

    # simply outputs contents of the file
    for line in file:
        print(line)


if __name__ == "__main__":
    main()
