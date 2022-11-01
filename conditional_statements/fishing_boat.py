budget = int(input())
season = input()
count_fishermen = int(input())

price_spring = 3000
price_summer_and_autumn = 4200
price_winter = 2600
ship_price = 0

if season == "Spring":
    if count_fishermen <= 6:
        ship_price = price_spring * 0.9
    elif 7 <= count_fishermen <= 11:
        ship_price = price_spring * 0.85
    else:
        ship_price = price_spring * 0.75

elif season == "Autumn" or season == "Summer":
    if count_fishermen <= 6:
        ship_price = price_summer_and_autumn * 0.9
    elif 7 <= count_fishermen <= 11:
        ship_price = price_summer_and_autumn * 0.85
    else:
        ship_price = price_summer_and_autumn * 0.75
elif season == "Winter":
    if count_fishermen <= 6:
        ship_price = price_winter * 0.9
    elif 7 <= count_fishermen <= 11:
        ship_price = price_winter * 0.85
    else:
        ship_price = price_winter * 0.75

if count_fishermen % 2 == 0 and season != "Autumn":
    total_price = ship_price * 0.95
else:
    total_price = ship_price

money_left = abs(budget - total_price)

if budget >= total_price:
    print(f"Yes! You have {money_left:.2f} leva left.")
else:
    print(f"Not enough money! You need {money_left:.2f} leva.")


