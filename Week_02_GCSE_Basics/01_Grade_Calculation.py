"""
TASK: 01 Grade Calculation

# Skills: Input, output, selection
Write a program that asks the user for a percentage grade and prints the corresponding letter grade:
- A: 80-100
- B: 60-79
- C: 40-59
- D: <40
Include a function def get_grade(score):

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
    # TODO: Write demonstration/testing code
    # If you want to delete all the code here and work just with a blank file go ahead, remember anything under the if __name__=="__main__":
    # will only run if this module is being run directly. So used this subprocedure to carry out testing if it is going to be an imported file.
    score = int(input("Enter score out of 100: "))
    gradeCalc = grade_calculator(score)

    print(gradeCalc)

def grade_calculator(score):
    if score >= 0 and score < 40:
        grade = "You got a D"
    elif score >= 40 and score < 60:
        grade = "You got a C"
    elif score >= 60 and score < 80:
        grade = "You got a B"
    elif score >= 80 and score <= 100:
        grade = "You got an A"
    else:
        grade = "Invalid score"


    return grade


if __name__ == "__main__":
    main()
