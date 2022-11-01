bad_grades_total = int(input())
grade_counter = 0
bad_grade_counter = 0
last_task = 0
total_grade_points = 0

while True:
#вход
# име на задача
# оценка

    task_name = input()
    if task_name == "Enough":
        average = total_grade_points / grade_counter
        print(f"Average score: {average:.2f}")
        print(f"Number of problems: {grade_counter}")
        print(f"Last problem: {last_task}")
        break
    grade = int(input())
    grade_counter += 1
    total_grade_points += grade
#ако оценката е по-малка и равна на 4 отбележи 1 лоша оценка
    if grade <= 4:
        bad_grade_counter += 1
#ако позволените лоши оценки съвшадат с общия брой лоши оценки
    if bad_grades_total == bad_grade_counter:
        print(f"You need a break, {bad_grade_counter} poor grades.")
        break
    last_task = task_name


