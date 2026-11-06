grade_1 = 7
grade_2 = 6
grade_3 = 8

average = (grade_1 + grade_2 + grade_3) / 3

print("Average:", average)

if grade_1 < 4 or grade_2 < 4 or grade_3 < 4:
    print("Gezakt!")
elif average >= 5.5:
    print("Geslaagd!")
else:
    print("Gezakt!")
