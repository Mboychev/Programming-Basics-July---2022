cake_lenght = int(input())
cake_width = int(input())

cake_total = cake_lenght * cake_width

while True:

    if cake_total <= 0:
        cake_total = -cake_total
        print(f"No more cake left! You need {cake_total} pieces more.")
        break

    pieces = input()

    if pieces == "STOP":
        print(f"{cake_total} pieces are left.")
        break

    pieces = int(pieces)
    cake_total -= pieces






