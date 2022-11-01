number_1 = int(input())
number_2 = int(input())

number_1_first_digit = number_1 // 1000
number_1_second_digit = (number_1 - (number_1_first_digit * 1000)) // 100
number_1_third_digit = (number_1 - (number_1_first_digit * 1000) - (number_1_second_digit * 100)) // 10
number_1_fourth_digit = (number_1 - (number_1_first_digit * 1000) - \
(number_1_second_digit * 100) - (number_1_third_digit * 10)) % 10

number_2_first_digit = number_2 // 1000
number_2_second_digit = (number_2 - (number_2_first_digit * 1000)) // 100
number_2_third_digit = (number_2 - (number_2_first_digit * 1000) - (number_2_second_digit * 100)) // 10
number_2_fourth_digit = (number_2 - (number_2_first_digit * 1000) - \
(number_2_second_digit * 100) - (number_2_third_digit * 10)) % 10


for i in range(number_1_first_digit, number_2_first_digit + 1):
    for j in range(number_1_second_digit, number_2_second_digit + 1):
        for k in range(number_1_third_digit, number_2_third_digit + 1):
            for v in range(number_1_fourth_digit, number_2_fourth_digit + 1):
                if i % 2 != 0 and j % 2 != 0 and k % 2 != 0 and v % 2 != 0:
                    print(f"{i}{j}{k}{v}", end = " ")


