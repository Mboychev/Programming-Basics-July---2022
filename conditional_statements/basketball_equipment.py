annual_fee = int(input())
sneakers = annual_fee - (annual_fee * 0.4)
outfit = sneakers - (sneakers * 0.2)
ball = (1/4) * outfit
accessories  = (1/5) * ball
total_equipment = annual_fee + sneakers + outfit + ball + accessories
print(total_equipment)