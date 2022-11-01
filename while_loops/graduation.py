studen_name = input()
year = 0

grades_total = 0
fails_counter = 0
average = 0

while year < 12:
    year += 1
    if fails_counter == 2:

        break

    grade = float(input())

    if grade < 4:
        fails_counter += 1
        year -= 1
    else:
        grades_total += grade


if fails_counter == 2:
    print(f"{studen_name} has been excluded at {year} grade")

else:
    average = grades_total/year
    print(f"{studen_name} graduated. Average grade: {average:.2f}")

