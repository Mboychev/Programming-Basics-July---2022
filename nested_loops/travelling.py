
total_saved_sum = 0

while True:

    destination = input()

    if destination == "End":
        break

    budget = float(input())


    while total_saved_sum < budget:

        saved_sum = float(input())
        total_saved_sum += saved_sum

    else:
        total_saved_sum = 0
        print(f"Going to {destination}!")




