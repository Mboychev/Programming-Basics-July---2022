import sys

max_number = -sys.maxsize
min_number = sys.maxsize

sign = True

while True:

    number = input()

    if number == "Stop":
        break

    number = int(number)

    if number > max_number:
        max_number = number
        sign = True

    if number < -min_number:
        min_number = number
        sign = False

if sign == True:
    print(f"{max_number}")
else:
    print(f"{min_number}")







