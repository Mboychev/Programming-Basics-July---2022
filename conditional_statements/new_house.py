flower_type = input()
flower_count = int(input())
budget = int(input())
total_price = 0

rose_price = 5
dahlia_price = 3.8
tulip_price = 2.8
narcissus_price = 3
gladiolus_price = 2.5

if flower_type == "Roses":
    if flower_count > 80:
        total_price = flower_count * rose_price * 0.9
    else:
        total_price = flower_count * rose_price

if flower_type == "Dahlias":
    if flower_count > 90:
        total_price = flower_count * dahlia_price * 0.85
    else:
        total_price = flower_count * dahlia_price

if flower_type == "Tulips":
    if flower_count > 80:
        total_price = flower_count * tulip_price * 0.85
    else:
        total_price = flower_count * tulip_price

if flower_type == "Narcissus":
    if flower_count < 120:
        total_price = flower_count * narcissus_price * 1.15
    else:
        total_price = flower_count * narcissus_price

if flower_type == "Gladiolus":
    if flower_count < 80:
        total_price = flower_count * gladiolus_price * 1.2
    else:
        total_price = flower_count * gladiolus_price
money_left = abs(budget - total_price)

if total_price <= budget:
    print(f"Hey, you have a great garden with {flower_count} {flower_type} and {money_left:.2f} leva left.")
else:
    print(f"Not enough money, you need {money_left:.2f} leva more.")


