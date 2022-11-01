actor_name = input()
initial_academy_points = float(input())
joury_count = int(input())

total_points = initial_academy_points

for i in range(joury_count):

    joury_name = input()
    points_given = float(input())

    current_points = ((len(joury_name) * points_given)/2)
    total_points = total_points + current_points

    if total_points >= 1250.5:
        break

if total_points < 1250.5:
    diff = 1250.5 - total_points
    print(f"Sorry, {actor_name} you need {diff:.1f} more!")

else:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")














