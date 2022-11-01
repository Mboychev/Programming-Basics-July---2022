lily_years = int(input())
washing_mashine_price = float(input())
toy_single_price = int(input())

money_per_year = 0
total_money = 0
toys_count = 0
brother_steal = 0

for i in range(1, lily_years + 1):

    if i % 2 == 0:
        money_per_year += 10
        total_money += money_per_year
        brother_steal += 1
    else:
        toys_count += 1

total = (total_money - brother_steal) + toys_count * toy_single_price

diff = abs(total - washing_mashine_price)

if total >= washing_mashine_price:

    print(f"Yes! {diff:.2f}")

else:
    print(f"No! {diff:.2f}")
