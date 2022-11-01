number_range = int(input())
the_bigest = 0
no_bigest = 0
numbers_sum = 0

for i in range(number_range):

    number = int(input())

    if number > the_bigest:

        the_bigest = number
        numbers_sum += number

    else:
        numbers_sum += number

no_bigest = numbers_sum - the_bigest

if the_bigest == no_bigest:
    print("Yes")
    print(f"Sum = {no_bigest}")

else:
    diff = abs(the_bigest - (no_bigest))
    print("No")
    print(f"Diff = {diff}")






