free_space_width = int(input())
free_space_lenght = int(input())
free_space_height = int(input())

total_space = free_space_height * free_space_width * free_space_lenght
total_used_space = 0
box_counter = 0
while True:

    count_boxes = input()

    if count_boxes == "Done":
        total_used_space = total_space - box_counter
        print(f"{total_used_space} Cubic meters left.")
        break

    count_boxes = int(count_boxes)
    box_counter += count_boxes

    if total_space <= box_counter:
        diff = abs(total_space - box_counter)
        print(f"No more free space! You need {diff} Cubic meters more.")
        break

