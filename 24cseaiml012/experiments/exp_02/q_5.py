marks = []
for i in range(1, 6):
    mark = int(input(f"Enter marks for subject {i} (out of 50): "))
    if 0 <= mark <= 50:
        marks.append(mark)
    else:
        print("Invalid input! Marks must be between 0 and 50.")
        exit()
total_marks = sum(marks)
max_marks = 5 * 50  
percentage = (total_marks / max_marks) * 100
if 90 <= percentage <= 100:
    grade = "O"
elif 80 <= percentage < 90:
    grade = "E"
elif 70 <= percentage < 80:
    grade = "A"
elif 60 <= percentage < 70:
    grade = "B"
elif 50 <= percentage < 60:
    grade = "C"
else:
    grade = "F"
print("\n--- Result ---")
print("Total Marks:", total_marks, "/", max_marks)
print("Percentage:", round(percentage, 2), "%")
print("Grade:", grade)