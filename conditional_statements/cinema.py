type = input()
rows = int(input())
cols = int(input())

income = 0
price = 0

if type == "Premiere":
    price = 12.00
elif type == "Normal":
    price = 7.50
elif type == "Discount":
    price = 5.00

income = price * rows * cols
print(f"{income:.2f}")