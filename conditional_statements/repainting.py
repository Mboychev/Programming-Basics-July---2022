count_naylon = int(input())
count_paint = int(input())
count_thinner = int(input())
labor = int(input())
sum_naylon = (count_naylon + 2) * 1.5
sum_paint = (count_paint * 1.1) * 14.5
sum_thinner = count_thinner * 5
bag = 0.4
total_materials = sum_naylon + sum_paint + sum_thinner + bag
labor_cost = (total_materials * 30/100) * labor
total = total_materials + labor_cost
print(total)



