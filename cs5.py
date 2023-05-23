print("Enter your current time below.")
hours = input("Hours: ")
minutes = input("Minutes: ")
seconds = input("Seconds: ")
h = int(hours) * 60 * 60
m = int(minutes) * 60
s = int(seconds)
day = 24 * 60 * 60
res = day - (h + m + s)
print("Remaining time in seconds: ", res)
