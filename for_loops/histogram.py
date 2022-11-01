count_number = int(input())

total_count_number = 0

count_n1 = 0
count_n2 = 0
count_n3 = 0
count_n4 = 0
count_n5 = 0

for i in range(count_number):
    number = int(input())

    if number < 200:
        count_n1 += 1

    elif 200 <= number <= 399:
        count_n2 += 1

    elif 400 <= number <= 599:
        count_n3 += 1

    elif 600 <= number <= 799:
        count_n4 += 1

    else:
        count_n5 += 1

p1 = count_n1 / count_number * 100
p2 = count_n2 / count_number * 100
p3 = count_n3 / count_number * 100
p4 = count_n4 / count_number * 100
p5 = count_n5 / count_number * 100

print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
print(f"{p4:.2f}%")
print(f"{p5:.2f}%")

