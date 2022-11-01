number1 = int(input())
number2 = int(input())
operator = input()
result = 0


if operator == "+":
    result = number1 + number2
    if result % 2 == 0:
        print(f"{number1} {operator} {number2} = {result} - even")
    else:
        print(f"{number1} {operator} {number2} = {result} - odd")
elif operator == "-":
    result = number1 - number2
    if result % 2 == 0:
        print(f"{number1} {operator} {number2} = {result} - even")
    else:
        print(f"{number1} {operator} {number2} = {result} - odd")
elif operator == "*":
    result = number1 * number2
    if result % 2 == 0:
        print(f"{number1} {operator} {number2} = {result} - even")
    else:
        print(f"{number1} {operator} {number2} = {result} - odd")
elif operator == "%" and number2 == 0:
    print(f"Cannot divide {number1} by zero")
elif operator == "%" and number2 != 0:
    result = number1 % number2
    print(f"{number1} % {number2} = {result}")
elif operator == "/" and number2 != 0:
    result = number1 / number2
    if result % 2 == 0:
        print(f"{number1} {operator} {number2} = {result:.2f}")
    else:
        print(f"{number1} {operator} {number2} = {result:.2f}")
elif number2 == 0 and operator == "/":
    print(f"Cannot divide {number1} by zero")

