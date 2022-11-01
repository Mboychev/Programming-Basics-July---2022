petar_budget = float(input())
count_gpu = int(input())
count_proccessors = int(input())
count_ram = int(input())



gpu_price = count_gpu * 250
processor_price = count_proccessors * (gpu_price * 0.35)
ram_price = count_ram * (gpu_price * 0.1)

total_price = gpu_price + processor_price + ram_price

if count_gpu > count_proccessors:
       total_price = total_price * 0.85


budget_left = abs(petar_budget - total_price)
if petar_budget >= total_price:
    print(f"You have {budget_left:.2f} leva left!")
else:
    print(f"Not enough money! You need {budget_left:.2f} leva more!")