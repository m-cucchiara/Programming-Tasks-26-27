"""
TASK: 06 Simple Login

# Skills: Selection, string comparison
Start with a correct username/password (extend if saved in a text file separately):
- Ask for login
- Print "Welcome" or "Access Denied {number} attempts remaining"
Only allow 3 attempts and close the file

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
    # TODO: Write demonstration/testing code
    # If you want to delete all the code here and work just with a blank file go ahead, remember anything under the if __name__=="__main__":
    # will only run if this module is being run directly. So used this subprocedure to carry out testing if it is going to be an imported file.
    usernames = [
    "alice_test",
    "bob_test",
    "charlie_test",
    "diana_test",
    ]

    passwords = [
    "TestPass_001!",
    "TestPass_002!",
    "TestPass_003!",
    "TestPass_004!",
    ]

    login_system(usernames, passwords)


def login_system(usernames, passwords):
    attempts = 3
    found = False



    while attempts != 0 or found == True:
        found = False

        userAttempt = input("Enter username: ")
        passAttempt = input("Enter password: ")

        for i in range (len(passwords)):
            if userAttempt == usernames[i] and passAttempt == passwords[i]:
                found = True


        if found == True:
            print ("Welcome")
            break

        else:
            attempts = attempts - 1
            print("Incorrect login details, ", attempts, "attempts remaining.")






if __name__ == "__main__":
    main()
