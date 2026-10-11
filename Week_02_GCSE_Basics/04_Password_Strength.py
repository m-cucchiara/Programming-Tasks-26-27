"""
TASK: 04 Password Strength

# Skills: Strings, loops, selection
Ask the user to enter a password, and check that they meet these conditions:
- At least 8 characters
- Contains a number
- Contains a captial and lower cased letter
- Extend for one special character
Print a response of weak, medium or strong for how many they pass.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
    # TODO: Write demonstration/testing code
    # If you want to delete all the code here and work just with a blank file go ahead, remember anything under the if __name__=="__main__":
    # will only run if this module is being run directly. So used this subprocedure to carry out testing if it is going to be an imported file.
    password = input("Enter password: ")

    passwordStrength = password_analyzer(password)
    if passwordStrength <= 1 and passwordStrength > 0:
        print("Weak")
    elif passwordStrength > 1 and passwordStrength < 4:
        print("Medium")
    else:
        print("Strong")

def password_analyzer(password):
    strength = 0
    lower = False
    upper = False
    numCheck = False
    specialChar = False

    for char in password:
        if char.isnumeric():
            numCheck = True
        if char.isupper():
            upper = True
        if char.islower():
            lower = True
        if not password.isalnum():
            specialChar = True

    if lower == True and upper == True:
        strength += 1
    if numCheck == True:
        strength += 1
    if specialChar == True:
        strength += 1
    if len(password) >= 8:
        strength = strength + 1



    return strength



if __name__ == "__main__":
    main()
