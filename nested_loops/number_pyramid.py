wall_heigh = int(input())
wall_width = int(input())
not_painted = int(input())
total_painted = wall_width * wall_heigh
percent_not_painted = total_painted * not_painted
total_painted = total_painted - percent_not_painted
current_painted = 0

while True:

    paint_liters = input()

    if paint_liters == "Tired!":
        diff = total_painted - current_painted
        print(f"{diff} quadratic m left.")
        break

    paint_liters = int(input())
    paint_liters = int(paint_liters)
    current_painted += paint_liters

    if total_painted >= current_painted:
        diff = total_painted - current_painted
        print(f"All walls are painted and you have {diff} l paint left!")
        break







    # При получаване на командата "Tired!":
# "{квадратни метри} quadratic m left."
# {квадратни метри} е повърхнината, която му остава да боядисана.
# Aко е останала боя в излишък:
# "All walls are painted and you have {литри боя} l
#  paint left!"
