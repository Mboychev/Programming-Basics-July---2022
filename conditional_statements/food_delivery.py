count_chicken = int(input())
count_fish = int(input())
count_veg = int(input())
price_chicken = count_chicken * 10.35
price_fish = count_fish * 12.4
price_veg = count_veg * 8.15
total_meals = price_chicken + price_fish + price_veg
price_dessert = total_meals * 20/100
delivery_price = 2.5
total = total_meals + price_dessert + delivery_price
print(total)
