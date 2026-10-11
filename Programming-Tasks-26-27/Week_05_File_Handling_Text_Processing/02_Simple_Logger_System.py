"""
TASK: 02 Simple Logger System

# Create a script that appends time-stamped log entries to a file.
Menu:
- Add Log
- View Log
- Clear Log

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""


import datetime

def main():
    # TODO: Write demonstration/testing code
    # If you want to delete all the code here and work just with a blank file go ahead, remember anything under the if __name__=="__main__":
    # will only run if this module is being run directly. So used this subprocedure to carry out testing if it is going to be an imported file.

    messageAdded = "" # placeholder so log_entry module doesnt crash

    fileName = "log.txt"

    # assigns dateLogged to date and time
    dateLogged = str(datetime.datetime.now())

    username = input("Enter username: ")

    # displays available choices
    print("1: View log")
    print("2: Add log")
    print("3: Clear log")
    print("4: Exit")

    choice = input("Enter choice: ")

    if choice >= "1" and choice <= "3": # only for choices that allows interaction with the log (1-3)
        if choice == "1":
            view_log(fileName)
        elif choice == "2":
            messageAdded = add_log()
        elif choice == "3":
            clear_log(fileName)

        log_entry(username, dateLogged, fileName, choice, messageAdded) # if a user interacted with the log, their user, date, time and action is logged
        print("Operation sucessful!")

    elif choice == "4":
        print("Exited program")
    else:
        print("Invalid input. Try again")
        main()  # recurses back to main() if theres an invalid input



def log_entry(username, dateLogged, fileName, choice, messageAdded):

    # subprogram logs each user's action
    file = open(fileName, "a")

    # writes start of log in the format date | Username: (username) | Action: (action)
    file.write(dateLogged)
    file.write(" | Username: ")
    file.write(username)
    file.write(" | Action: ")

    if choice == "1":
        file.write("Viewed log")    # logs that the user viewed logs
    elif choice == "2":
        file.write("Added message: ")   # logs that the user set a message
        file.write(messageAdded)
    elif choice == "3":
        file.write("Cleared log") # logs that the user cleared the logs

    file.write("\n")
    file.close()
    main()


def view_log(fileName):
    file = open(fileName, "r")

    # simply displays line in the logs.txt file
    for line in file:
        line = line.strip()
        print(line)


def add_log():
    messageAdded = input("Enter message: ")

    return messageAdded     # simply returns the message the user inputted, it is added to the logs via another subprogram

def clear_log(fileName):
    file = open(fileName, "w")

    file.write("") # simply empties the log.



if __name__ == "__main__":
    main()
