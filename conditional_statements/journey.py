budget = float(input())
season = input()
price = 0
destination = 0
type_rest = 0

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        price = budget * 0.3
    elif season == "winter":
        price = budget * 0.7
elif 100 < budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        price = budget * 0.4
    elif season == "winter":
        price = budget * 0.8
else:
    destination = "Europe"
    if season == "summer" or season == "winter":
        price = budget * 0.9
if season == "summer" and destination != "Europe":
    type_rest = "Camp"
elif season == "winter":
    type_rest = "Hotel"
else:
    type_rest = "Hotel"

print(f"Somewhere in {destination}")
print(f"{type_rest} - {price:.2f}")




