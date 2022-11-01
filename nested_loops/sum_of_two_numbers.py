start = int(input())
stop = int(input())
magic_number = int(input())

numbers_sum = 0
number_counter = 0
is_found = False

for first_number in range(start, stop + 1):
    for second_number in range(start, stop + 1):

        number_counter += 1
        numbers_sum = first_number + second_number

        if numbers_sum == magic_number:
            is_found = True
            print(f"Combination N:{number_counter} ({first_number} + {second_number} = {magic_number})")


        if is_found == True:
            break

    if is_found == True:
        break
else:

    print(f"{number_counter} combinations - neither equals {magic_number}")






