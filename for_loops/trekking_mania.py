count_groups = int(input())

total_count_people = 0
total_musala = 0
total_monblan = 0
total_kilimanjaro = 0
total_k2 = 0
total_everest = 0

for i in range(count_groups):

    count_people = int(input())

    total_count_people += count_people

    if count_people <= 5:  # Група до 5 човека – изкачват Мусала
        musala_climbers = count_people
        total_musala = total_musala + musala_climbers

    elif 6 <= count_people <= 12:  # Група от 6 до 12 човека – изкачват Монблан
        monblan_climbers = count_people
        total_monblan = total_monblan + monblan_climbers

    elif 13 <= count_people <= 25:  # Група от 13 до 25 човека – изкачват Килиманджаро
        kilimanjaro_climbers = count_people
        total_kilimanjaro = total_kilimanjaro + kilimanjaro_climbers

    elif 26 <= count_people <= 40:  # Група от 26 до 40 човека –  изкачват К2
        k2_climbers = count_people
        total_k2 = total_k2 + k2_climbers

    else:  # Група от 41 или повече човека – изкачват Еверест
        everest_climbers = count_people
        total_everest = total_everest + everest_climbers

musala = total_musala / total_count_people * 100
monblan = total_monblan / total_count_people * 100
kilimanjaro = total_kilimanjaro / total_count_people * 100
k2 = total_k2 / total_count_people * 100
everest = total_everest / total_count_people * 100

print(f"{musala:.2f}%")
print(f"{monblan:.2f}%")
print(f"{kilimanjaro:.2f}%")
print(f"{k2:.2f}%")
print(f"{everest:.2f}%")

