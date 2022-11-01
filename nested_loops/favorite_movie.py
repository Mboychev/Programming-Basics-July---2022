total_sum = 0
new_sum = 0
the_bigest = 0
big_counter = 0
small_counter = 0
blank_space = 0

for movie_counter in range(0, 7, 1):

    movie_counter += 1
    movie = input()

    if movie == "STOP":
        movie_counter -= 1
        break

    for letter in (movie):

        if letter == " ":
            blank_space += 1

        in_num = ord(letter)

        if 65 <= in_num <= 90:
            total_sum = in_num - (len(movie))
            big_counter += 1

        elif 97 <= in_num <= 122:
            total_sum = in_num - (2 * (len(movie)))
            small_counter += 1

        else:
            total_sum = in_num

        new_sum += total_sum


    if new_sum > the_bigest:
        the_bigest = new_sum
        new_sum = 0
        the_best_movie = movie


    else:
        new_sum = 0



if movie_counter == 7:
    print("The limit is reached.")


print(f"The best movie for you is {the_best_movie} with {the_bigest} ASCII sum.")

