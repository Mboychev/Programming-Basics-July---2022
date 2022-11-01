from math import ceil
series_name = input()
series_time = int(input())
break_time = int(input())

lunch_time = break_time / 8
rest_time = break_time / 4
time_to_watch = break_time - lunch_time - rest_time
time_left = abs(time_to_watch - series_time)
if time_to_watch >= series_time:
    print(f"You have enough time to watch {series_name} and left with {ceil(time_left)} minutes free time.")
else:
    print(f"You don't have enough time to watch {series_name}, you need {ceil(time_left)} more minutes.")
