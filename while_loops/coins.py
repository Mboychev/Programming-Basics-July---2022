import decimal
from decimal import Decimal

change = float(input())
coins_change = round(change * 100)
counter_unit = 0


while True:



    if coins_change < 1:
        print(counter_unit)
        break

    if coins_change >= 200:
        counter_unit += 1
        coins_change -= 200

    elif 100 <= coins_change < 200:
        counter_unit += 1
        coins_change -= 100


    elif 50 <= coins_change < 100:
        counter_unit += 1
        coins_change -= 50


    elif 20 <= coins_change < 50:
        counter_unit += 1
        coins_change -= 20

    elif 10 <= coins_change < 20:
        counter_unit += 1
        coins_change -= 10


    elif 5 <= coins_change < 10:
        counter_unit += 1
        coins_change -= 5

    elif 2 <= coins_change < 5:
        counter_unit += 1
        coins_change -= 2

    elif 1 <= coins_change < 2:
        counter_unit += 1
        coins_change -= 1

