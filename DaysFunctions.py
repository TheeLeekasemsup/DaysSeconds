import os
clearConsole = lambda: ('cls')
clearConsole()
print("                            ")
print("Seconds per day calculator")
print("                            ")
print("type y or n")
calcHours = input("Calculate Hours:".lower())
calcSeconds = input("Calculate Seconds:".lower())
calcMilliseconds = input("Calculate Milliseconds:".lower())
def seconds_per_day(days):
    hours = days * 24
    minutes = hours * 60
    seconds = minutes * 60
    dayWord = "day"
    if days <= 1:
        dayWord = "day"
    elif days > 1:
        dayWord = "days"
    if(calcHours == "y"):
        print("there is {0} hours in {1} {2}".format(hours,days,dayWord))   
    if(calcSeconds == "y"):
        print("there is {0} seconds in {1} {2}".format(seconds,days,dayWord))
    return seconds
selectDays = int(input("please select how many days you want to calculate:"))
dayWord = "day"
if selectDays <= 1:
    dayWord = "day"
elif selectDays > 1:
    dayWord = "days"

day_milliseconds = seconds_per_day(selectDays) * 1000
print("and \nthere is {0} milliseconds in {1} {2}".format(day_milliseconds,selectDays,dayWord))
