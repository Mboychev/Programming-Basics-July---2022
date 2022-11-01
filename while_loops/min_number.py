import sys

max_number = -sys.maxsize

sign = True

while True:

    number = input()

    if number == "Stop":
        break

    number = int(number)

    if number < min_number:
        min_number = number


print(f"{min_number}")
