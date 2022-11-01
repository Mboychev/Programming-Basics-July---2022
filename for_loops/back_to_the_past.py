inherited_money = float(input())
year_to_live = int(input())
total_money = inherited_money
ivan_years = 18

for current_year in range(1800, year_to_live + 1):


    if current_year % 2 == 0:
        total_money -= 12000

    elif current_year % 2 != 0:
        total_money -= 12000 + (50 * ivan_years)
    ivan_years += 1

if total_money >= 0:
    print(f"Yes! He will live a carefree life and will have {abs(total_money):.2f} dollars left.")

else:
    print(f"He will need {abs(total_money):.2f} dollars to survive.")