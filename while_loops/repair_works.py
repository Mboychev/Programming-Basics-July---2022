wall_heigh = int(input())
wall_width = int(input())
percent = int(input())

#колко площ трябва да се боядиса без прозорци и врати
total_area = (wall_heigh * wall_width * 4) - (wall_heigh * wall_width * 4) * (percent/100)


painted_at_turn = 0


while True:


    paint_litters = input()

    if paint_litters == "Tired!":

        print(f"{total_area:.0f} quadratic m left." )
        break

    paint_litters = int(paint_litters)
    total_area -= paint_litters

    if total_area < 0:
        print(f"All walls are painted and you have {abs(total_area):.0f} l paint left!" )
        break
    elif total_area == 0:
        print("All walls are painted! Great job, Pesho!")
        break



