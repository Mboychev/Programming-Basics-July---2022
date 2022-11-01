total_steps = 0
goal = 10000

while True:

    if total_steps >= goal:
        over_the_goal = total_steps - goal

        print(f"Goal reached! Good job!")
        print(f"{over_the_goal} steps over the goal!")
        break

    steps_per_day = input()

    if steps_per_day == "Going home":

        steps_per_day = input()
        steps_per_day = int(steps_per_day)
        total_steps += steps_per_day

        if total_steps < goal:

            diff = goal - total_steps
            print(f"{diff} more steps to reach goal.")
            break

        else:

            diff = total_steps - goal
            print(f"Goal reached! Good job!")
            print(f"{diff} steps over the goal!")
            break

    steps_per_day = int(steps_per_day)
    total_steps += steps_per_day




