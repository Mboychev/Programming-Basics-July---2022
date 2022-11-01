# name = input()
# user_password = input()
# password = input()
#
# while True:
#
#     if password == user_password:
#         print(f"Welcome {name}!")
#         break
#
#     password = input()

name = input()
user_password = input()
password = input()

while user_password != password:

    password = input()

print(f"Welcome {name}!")