total_money = 0

while True:

    money_increase = input()

    if money_increase == "NoMoreMoney":
        break

    money_increase = float(money_increase)

    if money_increase >= 0:
        total_money += money_increase
        print(f"Increase: {money_increase:.2f}")

    else:
        print("Invalid operation!")
        break

print(f"Total: {total_money:.2f}")
