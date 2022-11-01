excursion_price = float(input())
available_money = float(input())

spend_counter = 0
days_counter = 0
total_money = available_money

while True:

    days_counter += 1
    action = input()
    moved_sum = float(input())


    if action == "spend":
        spend_counter += 1
        total_money -= moved_sum

        if total_money <= 0:
            total_money = 0

    if action == "save":
        spend_counter = 0
        total_money += moved_sum

    if spend_counter == 5:
        print("You can't save the money.")
        print(days_counter)
        break

    if excursion_price <= total_money:
        print(f"You saved the money for {days_counter} days.")
        break

