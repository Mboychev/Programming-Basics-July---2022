excursion_price = float(input())
puzzle_count = int(input())
dolls_count = int(input())
teddy_count = int(input())
minions_count = int(input())
truck_count = int(input())

total_price = (puzzle_count * 2.6) + (dolls_count * 3) + (teddy_count * 4.1) + (minions_count * 8.2) + (truck_count * 2)
total_count = puzzle_count + dolls_count + teddy_count + minions_count + truck_count

if total_count >= 50:
    total_price = total_price * 0.75

total_price = total_price * 0.9

diff = abs(total_price - excursion_price)

if total_price >= excursion_price:
    print(f"Yes! {diff:.2f} lv left.")
else:
    print(f"Not enough money! {diff:.2f} lv needed.")