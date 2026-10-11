"""
TASK: 04 Temp Stats Csv

# Skills CSV read, simple maths
Go to this site https://www.metoffice.gov.uk/hadobs/hadcet/data/download.html and download the txt file
Daily Mean Temperature.
This file has dates and daily temperatures:
- Read all of the values
- Find the highest, lowest and average
- Print those three values
Extend - See how you can potentially use the dates to chart daily temp changes by years, by months
by day comparisons over time. Maybe chart them using mathplotlib or another library. Just see what you can do with it

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
    # TODO: Write demonstration/testing code
    # If you want to delete all the code here and work just with a blank file go ahead, remember anything under the if __name__=="__main__":
    # will only run if this module is being run directly. So used this subprocedure to carry out testing if it is going to be an imported file.
    file = open("meantemp_daily_totals.txt", "r")
    low, high, mean = average_min_max_calc(file)

    print("Lowest temperature: ", low)
    print("Highest temperature: ", high)
    print("Mean temperature: ", mean)

    file.close()

def average_min_max_calc(file):

    highestTemp = 0
    lowestTemp = 0
    total = 0
    count = 0

    for line in file:
        line = line.strip()
        line = line.strip(" ")
        line = line.split(" ")

        try:
            temp = float(line[-1:][0])
            total += temp
            count += 1

            if temp < lowestTemp:
                lowestTemp = temp

            if temp > highestTemp:
                highestTemp = temp


        except:
            pass

    meanTemp = total/count

    return lowestTemp, highestTemp, meanTemp








if __name__ == "__main__":
    main()
