# sum_number = int(input())
# new_number = int(input())
#
# total_sum = new_number
#
# while sum_number > total_sum:
#
#     new_number = int(input())
#     total_sum += new_number
#
# print(total_sum)

sum_number = int(input())
new_number = int(input())

total_sum = new_number

while True:

    if total_sum >= sum_number:
        print(total_sum)
        break

    new_number = int(input())
    total_sum += new_number