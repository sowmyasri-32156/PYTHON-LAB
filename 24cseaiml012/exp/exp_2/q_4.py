
weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

digit = int(input("Enter a digit (0-6): "))

if 0 <= digit <= 6:
    print("The day is:", weekdays[digit])
else:
    print("Invalid input! Please enter a digit between 0 and 6.")
