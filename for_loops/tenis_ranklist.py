from math import floor

count_turnaments = int(input())
starting_rank_points = int(input())


points = starting_rank_points
win_times = 0
final_times = 0
semi_times = 0

win_points = 0
finalist_points = 0
semi_points = 0

for i in range(count_turnaments):

    tournament_phase = input()

    if tournament_phase == "W":
        win_points = 2000
        win_times = win_times + 1
        points = points + win_points

    elif tournament_phase == "F":
        final_times = final_times + 1
        finalist_points = 1200
        points = points + finalist_points

    elif tournament_phase == "SF":
        semi_times = semi_times + 1
        semi_points = 720
        points = points + semi_points

average_points = ((win_times * win_points) + (final_times * finalist_points) \
                  + (semi_times * semi_points))/count_turnaments
percent = win_times / count_turnaments * 100
print(f"Final points: {points}")
print(f"Average points: {floor(average_points)}")
print(f"{percent:.2f}%")