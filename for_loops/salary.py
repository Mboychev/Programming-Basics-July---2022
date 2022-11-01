count_tabs = int(input())
salary = int(input())

facebook_penalty = 150
instagram_penalty = 100
reddit_penalty = 50

copy_salary = salary

for i in range(1, count_tabs + 1):

    if copy_salary > 0:

        site = input()


        if site == "Facebook":
            copy_salary = copy_salary - facebook_penalty

        elif site == "Instagram":
            copy_salary = copy_salary - instagram_penalty

        elif site == "Reddit":
            copy_salary = copy_salary - reddit_penalty
        if copy_salary <= 0:
            break

if copy_salary <= 0:
    print("You have lost your salary.")
else:
    print(copy_salary)


