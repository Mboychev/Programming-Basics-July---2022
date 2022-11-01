lenght_cm = int(input())
width_cm = int(input())
height_cm = int(input())
percent = float(input())
volume_cm = lenght_cm * width_cm * height_cm
volume_l = volume_cm / 1000
accessories_space = percent / 100
water_volume = volume_l * (1 - accessories_space)
print(water_volume)
