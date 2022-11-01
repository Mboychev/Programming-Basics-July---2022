deposit = float(input())
term = int(input())
annual_percent = float(input())
annual_interest = deposit * annual_percent / 100
month_interest = annual_interest / 12
total = deposit + term * month_interest
print(total)
