"""
TASK: 05 String Parser

# String Parser
Write a parser that:
- Accepts a sentence from the user.
- Splits it into words manually (not using split()).
- Outputs number of words + lshe ist of words.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
    # TODO: Write demonstration/testing code
    # If you want to delete all the code here and work just with a blank file go ahead, remember anything under the if __name__=="__main__":
    # will only run if this module is being run directly. So used this subprocedure to carry out testing if it is going to be an imported file.
    stringInput = input("Enter string: ")
    stringInput = stringInput + " "
    i = 0
    list = []
    word = ""

    for character in stringInput:
        if character == ' ':
            i += 1
            list.append(word)
            word = ""
        else:
            word = word + character


    return i, list

if __name__ == "__main__":
    string = main()

print("List of words: ", string[1])
print("Number of words is ", string[0])
