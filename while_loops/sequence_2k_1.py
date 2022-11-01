# number = int(input())
#
# counter = 1
#
# while number >= counter:
#
#     print(counter)
#     counter = counter * 2 + 1

number = int(input())

counter = 1

while True:

    if number < counter:
        break

    print(counter)
    counter = counter * 2 + 1