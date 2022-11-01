from math import pi
exam_hour = int(input())
exam_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

arrival_hour_min = arrival_hour * 60
exam_hour_min = exam_hour * 60
total_arrival = arrival_hour_min + arrival_minute
total_exam = exam_hour_min + exam_minute

diff = abs(total_exam - total_arrival)
# на време
if total_arrival <= total_exam and diff <= 1440:
    if diff == 0:
        print("On time")

    elif diff <= 30:
        mm = diff % 60
        print("On time")
        print(f"{mm} minutes before the start")

    elif diff < 60:
        mm = diff % 60
        print("Early")
        print(f"{mm} minutes before the start")

    else:
        hh = diff // 60
        mm = diff % 60
        print("Early")

        if mm < 10:
            print(f"{hh}:0{mm} hours before the start")

        else:
            print(f"{hh}:{mm} hours before the start")

if total_arrival > total_exam and diff <= 1440:

    diff = total_arrival - total_exam

    if diff < 60:
        mm = diff % 60
        print("Late")
        print(f"{mm} minutes after the start")

    else:
        hh = diff // 60
        mm = diff % 60
        print("Late")

        if mm < 10:
            print(f"{hh}:0{mm} hours after the start")
        else:
            print(f"{hh}:{mm} hours after the start")











# •	"Late", ако студентът пристига по-късно от часа на изпита;
# •	"On time", ако студентът пристига точно в часа на изпита или до 30 минути по-рано;
# •	"Early", ако студентът пристига повече от 30 минути преди часа на изпита.
# Ако студентът пристига с поне минута разлика от часа на изпита, отпечатайте на следващия ред:
# •	"mm minutes before the start" за идване по-рано с по-малко от час;
# •	"hh:mm hours before the start" за подраняване с 1 час или повече. Минутите винаги печатайте с 2 цифри, например "1:05”;
# •	 "mm minutes after the start" за закъснение под час;
