# anys_book = input()
# book_search = input()
# book_counter = 0
# book_found = False
#
# while book_search != "No More Books":
#
#     if book_search == anys_book:
#         book_found = True
#         break
#
#     book_counter += 1
#     book_search = input()
#
# if book_found:
#     print(f"You checked {book_counter} books and found it.")
# else:
#     print("The book you search is not here!")
#     print(f"You checked {book_counter} books.")
#

anys_book = input()
book_search = input()

book_counter = 0

while True:

    if book_search == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {book_counter} books.")
        break

    book_counter += 1
    book_search = input()

    if book_search == anys_book:
        print(f"You checked {book_counter} books and found it.")
        break