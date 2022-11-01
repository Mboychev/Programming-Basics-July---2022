month = input()
count_rent = int(input())

price_studio = 0
price_apartment = 0
total_studio = 0
total_apartment = 0

if month == "May" or month == "October":

    price_studio = 50
    price_apartment = 65

    if 7 < count_rent <= 14:
        total_studio = price_studio * 0.95 * count_rent
        total_apartment = price_apartment * count_rent

    elif count_rent > 14:
        total_studio = price_studio * 0.7 * count_rent
        total_apartment = price_apartment * 0.9 * count_rent

    else:
        total_studio = price_studio * count_rent
        total_apartment = price_apartment * count_rent


elif month == "June" or month == "September":

    price_studio = 75.20
    price_apartment = 68.70

    if count_rent > 14:
        total_studio = price_studio * count_rent * 0.8
        total_apartment = price_apartment * count_rent * 0.9
    else:
        total_studio = price_studio * count_rent
        total_apartment = price_apartment * count_rent

elif month == "July" or month == "August":

    price_studio = 76
    price_apartment = 77
    total_studio = price_studio * count_rent

    if count_rent > 14:
        total_apartment = price_apartment * count_rent * 0.9
    else:
        total_apartment = price_apartment * count_rent

print(f"Apartment: {total_apartment:.2f} lv.")
print(f"Studio: {total_studio:.2f} lv.")











