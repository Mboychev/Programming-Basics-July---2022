record_seconds = float(input())
distance_meters = float(input())
time_seconds = float(input())

# •	Ако Иван е подобрил Световния рекорд (времето му е по-малко от рекорда) отпечатваме:
# o	" Yes, he succeeded! The new world record is {времето на Иван} seconds."
# •	Ако НЕ е подобрил рекорда (времето му е по-голямо или равно на рекорда) отпечатваме:
# o	"No, he failed! He was {недостигащите секунди} seconds slower."
# Резултатът трябва да се форматира до втория знак след десетичната запетая.

time_ivan = distance_meters * time_seconds
slowed_times = distance_meters // 15
slowed_seconds = slowed_times * 12.5

total_time = time_ivan + slowed_seconds
diff = abs(total_time - record_seconds)
if record_seconds <= total_time:
    print(f"No, he failed! He was {diff:.2f} seconds slower.")

else:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")

