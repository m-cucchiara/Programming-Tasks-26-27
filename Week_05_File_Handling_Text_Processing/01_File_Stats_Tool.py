"""
TASK: 01 File Stats Tool

# Read a .txt file and compute:
Task:
- Number of lines
- Number of words
- Number of characters
- Most frequent word

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""


def main():
    # TODO: Write demonstration/testing code
    # If you want to delete all the code here and work just with a blank file go ahead, remember anything under the if __name__=="__main__":
    # will only run if this module is being run directly. So used this subprocedure to carry out testing if it is going to be an imported file.
    fileName = input("Enter file name: ")

    lineCount, wordCount = word_line_counter(fileName)
    charCount = char_counter(fileName)
    compressedList = run_length_encoding(fileName)
    mostUsedWord = highest_word_count(compressedList)


    print("The most used word is: ", mostUsedWord)
    print("Number of lines: ", lineCount)
    print("Number of words: ", wordCount)
    print("Number of characters", charCount)


def word_line_counter(fileName):
    lineCount = 0
    wordCount = 0

    try:
        file = open(fileName, "r")
        for line in file:
            lineCount += 1  # Adds every line
            line = line.strip()
            line = line.split(" ") # Turns each line into a list in order to get amount of words (considering this is not a CSV)
            for word in line:
                wordCount += 1  # Adds each word inside that list
    except:
        print("File not found, try again.")
        main()

    return lineCount, wordCount

def char_counter(fileName):
    charCount = 0

    file = open(fileName, "r")
    for line in file:
        line = line.strip()
        for char in line:
            charCount += 1      # Counts each character within the line

    return charCount

def run_length_encoding(fileName):

    # Compresses file using RLE

    list = []
    count = 1
    file = open(fileName, "r")

    for line in file:
        line = line.strip()
        line = line.split(" ")
        for i in range(1, len(line)):
            if line[i].lower() == line[i - 1].lower():  # if the previous word is equal to the word after it, the count is incremented
                count += 1
            else:
                list.append(str(count) + line[i])   # else concatenates count and the word, then stores it in a list
                count = 1   # makes count = 1 for the new word

    return list

def highest_word_count(compressedList):

    # Finds the highest word count

    countList = []
    count = 0
    highestValue = [0, 0]

    # for loops circulate through the compressed list

    for i in range(0, len(compressedList)):
        for j in range(1, len(compressedList)):
            if compressedList[i][1:] == compressedList[j][1:]:  # compares the word at position i, with every other word after it
                stringNum = (str(compressedList[j][:1]))    # stringnum is the count from before
                count += int(stringNum)

        countList.append([count, compressedList[i][1:]])    # stores each count and word in a record, then in a list
        count = 0

    for record in countList:
        if record[0] > highestValue[0]: # compares each count and outputs the most used word after circulating the list
            highestValue = record

    return highestValue[1]






if __name__ == "__main__":
    main()
