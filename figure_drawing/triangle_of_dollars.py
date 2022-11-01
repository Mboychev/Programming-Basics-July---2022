number = int(input())
stars = 0
for r in range(0, number):
    stars += 1
    for c in range(0, stars):
        print("$", end=" ")
    print()
