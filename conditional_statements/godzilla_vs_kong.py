from math import floor

record_in_sec = float(input())
distance_meteres = float(input())
time_per_meter_sec = float(input())

total_time = distance_meteres * time_per_meter_sec

slow = floor(distance_meteres / 50)
total_slow =  slow * 30
total = total_time + total_slow

if total < record_in_sec:

    total = print(f"Yes! The new record is {total:.2f} seconds.")

else:

    diff = abs(record_in_sec - total)
    print(f"No! He was {diff:.2f} seconds slower.")