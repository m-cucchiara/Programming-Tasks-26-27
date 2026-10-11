"""
TASK: 06 Temperature Converter

# Temperature Converter
Build a converter tool:
- Convert Celsius <-> Fahrenheit.
- Provide a looped menu.
- Validate user input.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
    # TODO: Write demonstration/testing code
    # If you want to delete all the code here and work just with a blank file go ahead, remember anything under the if __name__=="__main__":
    # will only run if this module is being run directly. So used this subprocedure to carry out testing if it is going to be an imported file.
    celsiusTemp = ""
    while celsiusTemp != "n":
        celsiusTemp = input("Enter a temperature in Celsius (enter n to exit): ")
        try:
            farenheitTemp = celsius_farenheit(float(celsiusTemp))
            print("Temperature is", farenheitTemp, "°F")
        except:
            print("Incorrect data type")

def celsius_farenheit(user_input):
    farenheitTemp = (user_input * (9/5)) + 32
    return farenheitTemp




if __name__ == "__main__":
    main()
