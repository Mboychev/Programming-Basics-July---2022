floors_count = int(input())
rooms_count = int(input())


for columns in range(floors_count, 0, -1):
    for rows in range(rooms_count):

        if columns % 2 == 0 and columns != floors_count:
            print(f"O{columns}{rows}", end = " ")

        elif columns == floors_count:
            print(f"L{columns}{rows}", end=" ")

        else:
            print(f"A{columns}{rows}", end=" ")
    print()

