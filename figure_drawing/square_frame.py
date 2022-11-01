square_frame_dimensions = int(input())

square_mid = square_frame_dimensions - 2
print("+",end= " ")

for dash in range(square_mid):
    print("-" , end= " ")
print("+")

for rows in range(square_mid):
    print("|",end= " ")
    for dash in range(square_mid):
        print("-" , end= " ")
    print("|")

print("+",end= " ")

for dash in range(square_mid):
    print("-" , end= " ")
print("+")
