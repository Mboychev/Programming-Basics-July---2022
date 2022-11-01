days = int(input())
room_type = input()
mark = input()

room_night = 18
apartment_night = 25
president_apartment_night = 35

price = 0
if room_type == "room for one person":

    if mark == "positive":
        price = (room_night * (days - 1)) * 1.25


    else:
        price = (room_night * (days - 1)) * 0.9


elif room_type == "apartment":

    if days < 10:

        if mark == "positive":
            price = (apartment_night * (days - 1)) * 0.7 * 1.25


        else:
            price = (apartment_night * (days - 1)) * 0.7 * 0.9


    elif 10 <= days <= 15:

        if mark == "positive":
            price = (apartment_night * (days - 1)) * 0.65 * 1.25


        elif mark == "negative":
            price = (apartment_night * (days - 1)) * 0.65 * 0.9

    else:

        if mark == "positive":
            price = (apartment_night * (days - 1)) * 0.5 * 1.25

        elif mark == "negative":
            price = (apartment_night * (days - 1)) * 0.5 * 0.9



elif room_type == "president apartment":

    if days < 10:

        if mark == "positive":
            price = (president_apartment_night * (days - 1)) * 0.9 * 1.25


        else:
            price = (president_apartment_night * (days - 1)) * 0.9 * 0.9


    elif 10 <= days <= 15:

        if mark == "positive":
            price = (president_apartment_night * (days - 1)) * 0.85 * 1.25


        elif mark == "negative":
            price = (president_apartment_night * (days - 1)) * 0.85 * 0.9

    else:

        if mark == "positive":
            price = (president_apartment_night * (days - 1)) * 0.8 * 1.25


        elif mark == "negative":
            price = (president_apartment_night * (days - 1)) * 0.8 * 0.9

print(f"{price:.2f}")
