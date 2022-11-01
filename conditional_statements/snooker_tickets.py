tournir_phase = input()
ticket_type = input()
ticket_count = int(input())
trophy_picture = input()
after_disc_price = 0

if ticket_type == "Standard":

    if tournir_phase == "Quarter final":
        ticket_price = 55.50

    elif tournir_phase == "Semi final":
        ticket_price = 75.88

    elif tournir_phase == "Final":
        ticket_price = 110.10

elif ticket_type == "Premium":

    if tournir_phase == "Quarter final":
        ticket_price = 105.20

    elif tournir_phase == "Semi final":
        ticket_price = 125.22

    elif tournir_phase == "Final":
        ticket_price = 160.66

elif ticket_type == "VIP":

    if tournir_phase == "Quarter final":
        ticket_price = 118.90

    elif tournir_phase == "Semi final":
        ticket_price = 300.40

    elif tournir_phase == "Final":
        ticket_price = 400

total_price = ticket_price * ticket_count

if 2500 < total_price <= 4000:
    after_disc_price = total_price * 0.9

elif total_price > 4000:
    after_disc_price = total_price * 0.75

elif total_price <= 2500:
    after_disc_price = total_price

if trophy_picture == 'Y' and total_price <= 4000:
    after_disc_price = after_disc_price + (40 * ticket_count)

elif trophy_picture == 'N' and total_price > 4000:
    after_disc_price = after_disc_price + (0 * ticket_count)

print(f"{after_disc_price:.2f}")

