print("Enter your current time below.")
hours = input("Hours: ")
minutes = input("Minutes: ")
seconds = input("Seconds: ")
day = 24 * 60 * 60
try:
    h = int(hours) * 60 * 60
    m = int(minutes) * 60
    s = int(seconds)
except ValueError as err:
    print("Error with data", err)
else:
    res = day - (h + m + s)
    print("Remaining time in seconds: ", res)